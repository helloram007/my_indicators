import unittest
from sd_reference import Candle as C,Zone,threshold,detect,patterns,candidate

class ZoneSPATests(unittest.TestCase):
    def test_buffer_arithmetic_and_tick_rounding(self):
        self.assertAlmostEqual(threshold(1.105,1.1,30,.0001,True),1.0985)
        self.assertAlmostEqual(threshold(1.105,1.1,30,.0001,False),1.1065)
        self.assertEqual(threshold(110,100,33,1,True),96)
        self.assertEqual(threshold(110,100,33,1,False),114)
        self.assertEqual(threshold(110,100,0,1,True),100)

    def test_invalid_base_metadata(self):
        for args in [(100,100,30,1,True),(99,100,30,1,True),(110,100,-1,1,True),(110,100,30,0,True)]:
            with self.assertRaises(ValueError):threshold(*args)

    def test_demand_wick_equality_and_own_timeframe(self):
        z=Zone(240,105,100,97,240,True)
        z.update(C(240,300,100,102,90,95),60)
        self.assertTrue(z.active)
        z.update(C(240,480,100,102,90,98),240)
        self.assertTrue(z.active)
        z.update(C(480,720,100,102,90,97),240)
        self.assertTrue(z.active)
        z.update(C(720,960,100,102,90,96),240,False)
        self.assertTrue(z.active)
        z.update(C(720,960,100,102,90,96),240)
        self.assertFalse(z.active)
        z.update(C(960,1200,100,105,99,104),240)
        self.assertFalse(z.active)
        self.assertEqual(z.ended,960)

    def test_supply_close_symmetric(self):
        z=Zone(60,110,105,113,60,False)
        z.update(C(60,120,110,120,105,113),60)
        self.assertTrue(z.active)
        z.update(C(120,180,110,120,105,114),60)
        self.assertFalse(z.active)

    def test_no_pre_creation_contact_or_retroactive_availability(self):
        z=Zone(240,105,100,97,480,True)
        self.assertFalse(z.contact(C(420,480,102,104,99,103)))
        self.assertTrue(z.contact(C(480,540,102,104,99,103)))

    def test_detector_needs_compact_base_and_closed_departure(self):
        base=[C(0,240,102,105,100,103),C(240,480,103,104,100,102)]
        departure=[C(480,720,102,109,102,108),C(720,960,108,115,108,114)]
        self.assertIsNone(detect(base,departure[:1],6))
        z=detect(base,departure,6,tick=.1)
        self.assertIsNotNone(z)
        self.assertEqual((z.top,z.low,z.invalid,z.created),(103,100,98.5,960))
        self.assertIsNone(detect(base,departure,1))

    def test_pattern_detectors_and_zero_body(self):
        prev=C(0,60,110,111,99,100)
        bull=C(60,120,99,113,98,112)
        self.assertIn('Engulf',patterns(bull,prev)[0])
        self.assertNotIn('Engulf',patterns(C(60,120,101,113,98,109),prev)[0])
        pin=C(60,120,108,110,90,109)
        self.assertIn('Pin',patterns(pin,prev)[0])
        self.assertEqual(patterns(C(60,120,100,110,90,100),prev),(set(),set()))

    def test_piercing_midpoint_gap_and_bear_counterpart(self):
        prev=C(0,60,110,111,99,100)
        self.assertNotIn('Piercing',patterns(C(60,120,100,108,99,105),prev)[0])
        current=C(60,120,100,109,99,108)
        self.assertIn('Piercing',patterns(current,prev)[0])
        self.assertNotIn('Piercing',patterns(current,prev,strict_gap=True)[0])
        prev=C(0,60,100,111,99,110); current=C(60,120,110,111,101,102)
        self.assertNotIn('Dark cloud',patterns(current,prev)[1])
        self.assertIn('Dark cloud',patterns(current,prev,True)[1])

    def test_htf_gate_location_and_invalidation_precedence(self):
        prev=C(240,300,110,111,99,100)
        c=C(300,360,99,113,98,112)
        z=Zone(60,102,98,96,240,True)
        self.assertIn('Engulf',candidate(1,c,prev,[z]))
        self.assertFalse(candidate(-1,c,prev,[z]))
        self.assertFalse(candidate(0,c,prev,[z]))
        self.assertFalse(candidate(1,c,prev,[]))
        z.active=False
        self.assertFalse(candidate(1,c,prev,[z]))

    def test_pin_requires_rejection_wick_contact(self):
        prev=C(0,60,110,111,99,100)
        pin=C(60,120,108,110,90,109)
        lower_zone=Zone(60,99,90,87,60,True)
        upper_zone=Zone(60,110,109,108,60,True)
        self.assertIn('Pin',candidate(1,pin,prev,[lower_zone]))
        self.assertNotIn('Pin',candidate(1,pin,prev,[upper_zone]))

    def test_zone_lifecycles_independent_and_fixed(self):
        h4=Zone(240,105,100,97,240,True)
        h1=Zone(60,105,100,97,240,True)
        c=C(240,300,100,101,90,96)
        for z in [h4,h1]:z.update(c,60)
        self.assertTrue(h4.active);self.assertFalse(h1.active)
        self.assertEqual((h4.top,h4.low,h4.invalid),(105,100,97))

if __name__=='__main__':unittest.main()
