import random
import unittest
from bias_reference import Bar, Bias

class BiasTests(unittest.TestCase):
    def series(self, highs, lows=None, **kwargs):
        lows = lows if lows is not None else [0]*len(highs)
        e = Bias(**kwargs)
        for t, (h, l) in enumerate(zip(highs, lows)):
            e.push(Bar(t, h, l, (h+l)/2))
        return e

    def test_confirmation_delay_and_failed_candidate(self):
        e = self.series([9,10,13,11,12])
        self.assertTrue(all(x[5] is None for x in e.events[:4]))
        self.assertEqual((e.events[4][5],e.events[4][7]), (13,2))
        self.assertEqual(self.series([9,10,13,11,14]).highs, [])
        e = self.series([10]*5, [7,6,3,5,4])
        self.assertEqual(e.lows, [3])

    def test_strict_tie_and_dual(self):
        self.assertEqual(self.series([9,10,13,13,12]).highs, [])
        e = self.series([9,10,13,11,12], [7,6,3,5,4])
        self.assertTrue(e.events[-1][8])
        self.assertEqual((e.highs,e.lows), ([],[]))

    def test_direction_and_mixed(self):
        e = Bias(); e.highs=[100]; e.lows=[90,95]
        self.assertEqual(e.transition(105,high=110)[:2],(1,95))
        e = Bias(); e.highs=[110]; e.lows=[95,90]
        self.assertEqual(e.transition(94,high=100)[:2],(-1,100))
        e = Bias(); e.highs=[100]; e.lows=[95,90]
        self.assertEqual(e.transition(105,high=110)[0],0)

    def test_invalidation_equality_no_rearm_and_fresh_recovery(self):
        e = Bias(); e.highs=[100]; e.lows=[90,95]; e.transition(105,high=110)
        self.assertEqual(e.transition(95)[0],1)
        self.assertEqual(e.transition(94)[0],0)
        self.assertEqual(e.transition(105)[0],0)
        e.transition(108,low=97)
        self.assertEqual(e.transition(108,high=112)[:2],(1,97))

    def test_bear_invalidation(self):
        e=Bias(); e.highs=[110]; e.lows=[95,90]; e.transition(94,high=100)
        self.assertEqual(e.transition(100)[0],-1)
        self.assertEqual(e.transition(101)[0],0)

    def test_same_close_priority(self):
        e=Bias(); e.highs=[100]; e.lows=[90,95]; e.transition(105,high=110)
        self.assertEqual(e.transition(94,high=112)[:2],(0,None))
        self.assertEqual(e.transition(108)[0],0)

    def test_already_invalidated(self):
        e=Bias(); e.highs=[100]; e.lows=[90,95]
        self.assertEqual(e.transition(94,high=110)[2],'ALREADY_INVALIDATED')

    def test_warmup_duplicates_open_bar_and_quality_latch(self):
        e=Bias(); b=Bar(0,10,0,5)
        self.assertEqual(e.push(b)[1],2)
        self.assertIsNone(e.push(b))
        self.assertIsNone(e.push(Bar(1,20,0,5,False)))
        self.assertEqual(len(e.events),1)
        self.assertEqual(e.push(Bar(1,1,2,3))[9],'DATA_ERROR_RELOAD_REQUIRED')
        self.assertEqual(e.push(Bar(2,10,0,5))[1],2)

    def test_prefix_reload_parity_and_strengths(self):
        rng=random.Random(14)
        bars=[Bar(i,100+rng.random()*20,70+rng.random()*20,95) for i in range(90)]
        for strength in [(2,2),(1,3)]:
            full=Bias(*strength)
            for b in bars: full.push(b)
            for end in range(1,len(bars)+1):
                replay=Bias(*strength)
                for b in bars[:end]: replay.push(b)
                self.assertEqual(replay.events,full.events[:end])

    def test_raw_ohlc_bullish_integration(self):
        # Single-sided pivots alternate while both pairs rise. No future bar needed.
        e=self.series([105,110,106,104,108,115,110,108,112],
                      [96,98,95,90,96,100,98,95,100],left=1,right=1)
        self.assertTrue(any(x[1]==1 for x in e.events))
        for event in e.events:
            if event[7] is not None: self.assertEqual(event[0]-event[7],1)

if __name__=='__main__': unittest.main()
