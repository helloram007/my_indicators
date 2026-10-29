"""Synthetic cross-timeframe oracle checks; not TradingView scheduling tests."""
import unittest
import random
from bias_reference import Bias, Bar

class MultiTimeframeTests(unittest.TestCase):
    def data(self):
        rng = random.Random(51)
        bars=[]
        for i in range(96):
            c=100+rng.uniform(-9,9)
            bars.append(Bar((i+1)*60,c+2,c-2,c))
        four=[]
        for i in range(0,len(bars),4):
            group=bars[i:i+4]
            four.append(Bar(group[-1].time,max(b.high for b in group),min(b.low for b in group),group[-1].close))
        return bars,four

    def run_engine(self,bars,left=2,right=2):
        engine=Bias(left,right)
        for bar in bars: engine.push(bar)
        return engine.events

    def test_independent_strengths_leave_4h_unchanged(self):
        hourly,four=self.data()
        baseline=self.run_engine(four)
        one_default=self.run_engine(hourly)
        one_alternate=self.run_engine(hourly,1,3)
        self.assertNotEqual(one_default,one_alternate)
        self.assertEqual(baseline,self.run_engine(four))

    def test_projection_on_15m_never_publishes_before_hourly_close(self):
        hourly,_=self.data()
        events=self.run_engine(hourly)
        # At chart-bar OPEN t, only snapshots whose source close <= t are available.
        for t in range(0,hourly[-1].time+15,15):
            known=[e for e in events if e[0] <= t]
            if known:
                latest=known[-1]
                self.assertLessEqual(latest[0],t)
                self.assertLess(t-latest[0],60)
                if latest[7] is not None:
                    self.assertEqual(latest[0]-latest[7],120)
            else:
                self.assertLess(t,60)

    def test_separate_publication_clocks_and_prefixes(self):
        hourly,four=self.data()
        full1=self.run_engine(hourly)
        full4=self.run_engine(four)
        for end in [8,20,48,96]:
            prefix1=self.run_engine(hourly[:end])
            prefix4=self.run_engine(four[:end//4])
            self.assertEqual(prefix1,full1[:end])
            self.assertEqual(prefix4,full4[:end//4])
        self.assertEqual(len(full1),4*len(full4))

    def test_three_independent_clocks_and_fifteen_minute_confirmation(self):
        rng=random.Random(71)
        quarter=[]
        for i in range(128):
            close=100+rng.uniform(-10,10)
            quarter.append(Bar((i+1)*15,close+2,close-2,close))
        def aggregate(n):
            return [Bar(g[-1].time,max(b.high for b in g),min(b.low for b in g),g[-1].close)
                    for i in range(0,len(quarter),n) if len(g:=quarter[i:i+n])==n]
        events15=self.run_engine(quarter)
        events1=self.run_engine(aggregate(4))
        events4=self.run_engine(aggregate(16))
        self.assertEqual((len(events15),len(events1),len(events4)),(128,32,8))
        confirmed=[e for e in events15 if e[7] is not None]
        self.assertTrue(confirmed)
        self.assertTrue(all(e[0]-e[7]==30 for e in confirmed))
        # Altering only the 15m extractor does not alter either higher-timeframe input or oracle.
        self.assertNotEqual(events15,self.run_engine(quarter,1,3))
        self.assertEqual(events1,self.run_engine(aggregate(4)))
        self.assertEqual(events4,self.run_engine(aggregate(16)))

    def test_open_15m_updates_cannot_change_published_history(self):
        engine=Bias()
        for i in range(20): engine.push(Bar((i+1)*15,110+(i%3),90-(i%4),100))
        published=list(engine.events)
        for high,low,close in [(120,80,115),(130,70,75),(140,60,100)]:
            self.assertIsNone(engine.push(Bar(315,high,low,close,False)))
            self.assertEqual(engine.events,published)
        self.assertIsNotNone(engine.push(Bar(315,140,60,100,True)))
        self.assertEqual(engine.events[:-1],published)

    def test_quarter_hour_prefix_parity_with_alternate_strengths(self):
        rng=random.Random(72)
        bars=[]
        for i in range(64):
            close=100+rng.uniform(-10,10)
            bars.append(Bar((i+1)*15,close+2,close-2,close))
        for left,right in [(2,2),(3,1)]:
            full=self.run_engine(bars,left,right)
            for count in range(1,len(bars)+1):
                self.assertEqual(self.run_engine(bars[:count],left,right),full[:count])

if __name__=='__main__': unittest.main()
