"""Independent zone/SPA oracle. No dependencies and no TradingView execution."""
from dataclasses import dataclass
from decimal import Decimal, ROUND_FLOOR, ROUND_CEILING

@dataclass(frozen=True)
class Candle:
    opened: int
    closed: int
    open: float
    high: float
    low: float
    close: float

def threshold(high, low, percent, tick, demand):
    h,l,k,t=map(lambda x:Decimal(str(x)),(high,low,percent,tick))
    if h <= l or k < 0 or t <= 0: raise ValueError('invalid base or metadata')
    raw=l-(h-l)*k/100 if demand else h+(h-l)*k/100
    return float((raw/t).to_integral_value(rounding=ROUND_FLOOR if demand else ROUND_CEILING)*t)

@dataclass
class Zone:
    timeframe: int
    top: float
    low: float
    invalid: float
    created: int
    demand: bool
    active: bool=True
    ended: int|None=None

    def update(self,candle, timeframe, final=True):
        if timeframe != self.timeframe or not final or candle.closed <= self.created: return
        if self.active and (candle.close < self.invalid if self.demand else candle.close > self.invalid):
            self.active=False
            self.ended=candle.closed

    def contact(self,candle,wick_only=False):
        hi=min(candle.open,candle.close) if wick_only and self.demand else candle.high
        lo=max(candle.open,candle.close) if wick_only and not self.demand else candle.low
        return self.active and candle.opened >= self.created and lo <= self.top and hi >= self.low

def detect(base, departure, atr, percent=30,tick=.00001):
    if len(departure)!=2 or atr<=0 or not base: return None
    if any(c.high<=c.low or abs(c.close-c.open)>(c.high-c.low)*.5 for c in base): return None
    high=max(c.high for c in base);low=min(c.low for c in base)
    if high-low>1.2*atr: return None
    a,b=departure
    if any(c.high<=c.low or abs(c.close-c.open)<.5*(c.high-c.low) for c in departure): return None
    if a.close>a.open and b.close>b.open and b.close>high and b.close-a.open>=atr:
        return Zone(240,max(max(c.open,c.close) for c in base),low,threshold(high,low,percent,tick,True),b.closed,True)
    if a.close<a.open and b.close<b.open and b.close<low and a.open-b.close>=atr:
        return Zone(240,high,min(min(c.open,c.close) for c in base),threshold(high,low,percent,tick,False),b.closed,False)
    return None

def patterns(c,p,dark_cloud=False,strict_gap=False):
    r=c.high-c.low;b=abs(c.close-c.open);pb=abs(p.close-p.open)
    if r<=0 or b<=0:return set(),set()
    u=c.high-max(c.open,c.close);w=min(c.open,c.close)-c.low
    bull,bear=set(),set()
    if w>=2*b and w>=.6*r and u<=.2*r and c.close>=c.low+.65*r:bull.add('Pin')
    if u>=2*b and u>=.6*r and w<=.2*r and c.close<=c.low+.35*r:bear.add('Pin')
    if pb>0 and b>=1.2*pb and b>=.6*r:
        if c.close>c.open and p.close<p.open and c.open<=p.close and c.close>=p.open:bull.add('Engulf')
        if c.close<c.open and p.close>p.open and c.open>=p.close and c.close<=p.open:bear.add('Engulf')
    if p.close<p.open and c.close>c.open and (c.open<p.low if strict_gap else c.open<=p.close) and (p.open+p.close)/2<c.close<p.open:bull.add('Piercing')
    if dark_cloud and p.close>p.open and c.close<c.open and (c.open>p.high if strict_gap else c.open>=p.close) and p.open<c.close<(p.open+p.close)/2:bear.add('Dark cloud')
    return bull,bear

def candidate(bias,candle,previous,zones,dark_cloud=False):
    bull,bear=patterns(candle,previous,dark_cloud)
    wanted=bull if bias==1 else bear if bias==-1 else set()
    hits=set()
    for z in zones:
        if z.demand != (bias==1):continue
        if 'Pin' in wanted and z.contact(candle,True):hits.add('Pin')
        if z.contact(candle) or z.contact(previous):hits |= wanted-{'Pin'}
    return hits
