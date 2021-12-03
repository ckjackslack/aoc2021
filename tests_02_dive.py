import unittest
from _02_dive import (Position, ExtraPosition,
    calculate_final_position)

class Test02Dive(unittest.TestCase):
    def setUp(self):
        self._commands1 = ['forward 1', 'down 2', 'up 3']
        self._commands2 = ['forward 5', 'down 5',
            'forward 8', 'up 3', 'down 8', 'forward 2']
    def test_position_calculation(self):
        ipos = Position()
        assert ipos.horizontal == 0
        assert ipos.depth == 0
        fpos = calculate_final_position(ipos,
            self._commands1)
        self.assertEqual(fpos.horizontal, 1)
        self.assertEqual(fpos.depth, -1)
        self.assertEqual(fpos.get_result(), -1)
    def test_extraposition_calculation(self):
        ipos = ExtraPosition()
        assert ipos.horizontal == 0
        assert ipos.depth == 0
        assert ipos.aim == 0
        fpos = calculate_final_position(ipos,
            self._commands2)
        self.assertEqual(fpos.horizontal, 15)
        self.assertEqual(fpos.depth, 60)
        self.assertEqual(fpos.get_result(), 900)