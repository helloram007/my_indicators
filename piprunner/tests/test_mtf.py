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

if __name__=='__main__': unittest.main()
