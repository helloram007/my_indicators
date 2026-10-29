"""Independent Python oracle for B4H v0; not a Pine compiler or emulator."""
from dataclasses import dataclass
from math import isfinite

@dataclass(frozen=True)
class Bar:
    time: int
    high: float
    low: float
    close: float
    final: bool = True

class Bias:
    def __init__(self, left=2, right=2):
        if not 1 <= left <= 20 or not 1 <= right <= 20:
            raise ValueError('invalid strength')
        self.left, self.right = left, right
        self.bars, self.highs, self.lows, self.events = [], [], [], []
        self.state, self.protection = 2, None
        self.blocked = False
        self.reason = 'INSUFFICIENT_STRUCTURE'

    def transition(self, close, high=None, low=None):
        old = self.state
        broken = ((old == 1 and close < self.protection) or
                  (old == -1 and close > self.protection))
        if high is not None:
            self.highs.append(high)
        if low is not None:
            self.lows.append(low)
        if broken:
            self.state, self.protection = 0, None
            self.reason = 'CLOSE_BELOW_PROTECTED_LOW' if old == 1 else 'CLOSE_ABOVE_PROTECTED_HIGH'
        elif len(self.highs) < 2 or len(self.lows) < 2:
            self.state, self.protection, self.reason = 2, None, 'INSUFFICIENT_STRUCTURE'
        elif high is not None or low is not None or self.state == 2:
            hp, h = self.highs[-2:]
            lp, l = self.lows[-2:]
            bull, bear = h > hp and l > lp, h < hp and l < lp
            self.state = 1 if bull and close >= l else -1 if bear and close <= h else 0
            self.protection = l if self.state == 1 else h if self.state == -1 else None
            self.reason = ('HH_AND_HL' if self.state == 1 else 'LH_AND_LL' if self.state == -1
                           else 'ALREADY_INVALIDATED' if bull or bear else 'MIXED_OR_EQUAL_STRUCTURE')
        return self.state, self.protection, self.reason

    def push(self, b):
        if not b.final:
            return None
        if self.bars and b.time == self.bars[-1].time:
            return None
        if self.bars and b.time < self.bars[-1].time:
            raise ValueError('out of order')
        self.bars.append(b)
        if not all(isfinite(x) for x in [b.high, b.low, b.close]) or not b.low <= b.close <= b.high:
            self.blocked = True
        hp = lp = origin = None
        dual = False
        if not self.blocked and len(self.bars) > self.left + self.right:
            p = len(self.bars) - 1 - self.right
            candidate = self.bars[p]
            neighbors = self.bars[p-self.left:p] + self.bars[p+1:p+self.right+1]
            ph = all(candidate.high > x.high for x in neighbors)
            pl = all(candidate.low < x.low for x in neighbors)
            dual = ph and pl
            hp = candidate.high if ph and not dual else None
            lp = candidate.low if pl and not dual else None
            origin = candidate.time if hp is not None or lp is not None else None
        if self.blocked:
            self.state, self.protection, self.reason = 2, None, 'DATA_ERROR_RELOAD_REQUIRED'
        else:
            self.transition(b.close, hp, lp)
        event = (b.time, self.state, self.protection, tuple(self.highs[-2:]),
                 tuple(self.lows[-2:]), hp, lp, origin, dual, self.reason)
        self.events.append(event)
        return event
