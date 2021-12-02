import unittest
from aoc_helpers import (get_numbers_from_sliding_window,
    sum_sublists)

class TestAOCHelpers(unittest.TestCase):
    def test_get_numbers_from_sliding_window(self):
        report = [
            199, 200, 208,
            210, 200, 207,
            240, 269, 260, 263
        ]
        out = get_numbers_from_sliding_window(report)
        out = list(sum_sublists(out))
        expected = [607, 618, 618, 617, 647, 716, 769, 792]
        self.assertEqual(out, expected)

