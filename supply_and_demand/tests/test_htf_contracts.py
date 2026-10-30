"""Source contract checks only; compile/replay in TradingView separately."""
from pathlib import Path
import subprocess
import sys
import unittest
ROOT = Path(__file__).resolve().parents[1]

class HTFContracts(unittest.TestCase):
    def test_generated_consumers_match_canonical_sources(self):
        subprocess.run([sys.executable, str(ROOT/'tools/build_indicator.py'), '--check'], check=True)

    def test_all_confirmed_fields_offset_in_source_context(self):
        source = (ROOT/'src/HTFStructure.pine').read_text(encoding='utf-8')
        output = source.split('export confirmed', 1)[1].splitlines()[-1].strip()
        fields = output[1:-1].split(', ')
        self.assertEqual(len(fields), 15)
        self.assertTrue(all(field.endswith('[1]') for field in fields))
        self.assertNotIn('if barstate.isconfirmed', source)

    def test_annotation_coordinates_are_source_timestamps(self):
        view = (ROOT/'src/htf_structure_view.pine.inc').read_text(encoding='utf-8')
        self.assertIn('label.new(highPivotTime, lastHigh', view)
        self.assertIn('label.new(lowPivotTime, lastLow', view)
        self.assertEqual(view.count('label.new(sourceOpen,'), 2)
        self.assertEqual(view.count('xloc = xloc.bar_time'), 4)
        self.assertNotIn('label.new(bar_index', view)
        self.assertNotIn('plotshape(', view)

    def test_pivot_time_is_taken_from_pivot_not_confirmation_bar(self):
        source = (ROOT/'src/HTFStructure.pine').read_text(encoding='utf-8')
        self.assertIn('highPivotTime := time[rightBars]', source)
        self.assertIn('lowPivotTime := time[rightBars]', source)

    def test_event_delivery_and_request_contract(self):
        view = (ROOT/'src/htf_structure_view.pine.inc').read_text(encoding='utf-8')
        self.assertIn('sourceOpen != sourceOpen[1]', view)
        self.assertIn('bool emit = newSnapshot and barstate.isconfirmed', view)
        self.assertIn('confirmed(leftBars, rightBars), gaps = barmerge.gaps_off, lookahead = barmerge.lookahead_on', view)
        self.assertIn('timeframe.in_seconds(htf) < timeframe.in_seconds()', view)

if __name__ == '__main__':
    unittest.main()
