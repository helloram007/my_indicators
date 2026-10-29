import unittest
from break_reference import BreakOverlay

class BreakTests(unittest.TestCase):
    def test_bos_and_choch_are_relative_to_prior_bias(self):
        for bias, expected in [(1,1),(-1,2),(0,3),(2,3)]:
            self.assertEqual(BreakOverlay().update(100,111,bias,high=(10,110)),expected)
        for bias, expected in [(-1,-1),(1,-2),(0,-3),(2,-3)]:
            self.assertEqual(BreakOverlay().update(100,89,bias,low=(11,90)),expected)

    def test_equal_close_does_not_break(self):
        overlay=BreakOverlay()
        self.assertEqual(overlay.update(109,110,-1,high=(10,110)),0)
        self.assertEqual(overlay.update(110,111,-1,high=(10,110)),2)

    def test_one_event_per_pivot_and_fresh_identity(self):
        overlay=BreakOverlay()
        self.assertEqual(overlay.update(100,111,1,high=(10,110)),1)
        self.assertEqual(overlay.update(100,111,1,high=(10,110)),0)
        self.assertEqual(overlay.update(100,111,1,high=(20,110)),1)

    def test_no_retroactive_cross_and_invalid_data(self):
        overlay=BreakOverlay()
        self.assertEqual(overlay.update(112,113,1,high=(10,110)),0)
        self.assertEqual(overlay.update(100,111,1,high=(10,110),valid=False),0)
        overlay.discover(111,high=(10,110))
        self.assertEqual(overlay.update(100,111,1,high=(10,110)),0)

    def test_overlay_leaves_bias_oracle_unchanged(self):
        from bias_reference import Bias, Bar
        import random
        rng=random.Random(8)
        plain, annotated=Bias(),Bias()
        overlay=BreakOverlay()
        for i in range(100):
            close=100+rng.uniform(-5,5)
            bar=Bar(i,close+2,close-2,close)
            expected=plain.push(bar)
            old=annotated.state
            h=(len(annotated.highs),annotated.highs[-1]) if annotated.highs else None
            l=(len(annotated.lows),annotated.lows[-1]) if annotated.lows else None
            prev=annotated.bars[-1].close if annotated.bars else close
            overlay.update(prev,close,old,h,l)
            self.assertEqual(annotated.push(bar),expected)

if __name__=='__main__': unittest.main()
