import unittest
from typing import List
from ShortestPathFinder import *

class TestShortestPathFinder(unittest.TestCase):
    def test_directions_are_converted_to_list(self):
        test_input= "R5, L5, R5, R3"
        finder = ShortestPathFinder(test_input)
        self.assertIsInstance(finder.directions, List)
        self.assertEqual(4, len(finder.directions))

    def test_facing_north_initially(self):
        finder = ShortestPathFinder("")
        self.assertEqual("N", finder.current_direction)

    def test_get_current_index_for_all_cardinals(self):
        finder = ShortestPathFinder("")
        self.assertEqual(0, finder.get_current_index())
        finder.current_direction = "E"
        self.assertEqual(1, finder.get_current_index())
        finder.current_direction = "S"
        self.assertEqual(2, finder.get_current_index())
        finder.current_direction = "W"
        self.assertEqual(3, finder.get_current_index())

    def test_turn_right(self):
        finder = ShortestPathFinder("")
        finder.turn_right()
        self.assertEqual("E", finder.current_direction)
        finder.turn_right()
        self.assertEqual("S", finder.current_direction)
        finder.turn_right()
        self.assertEqual("W", finder.current_direction)
        finder.turn_right()
        self.assertEqual("N", finder.current_direction)

    def test_turn_left(self):
        finder = ShortestPathFinder("")
        finder.turn_left()
        self.assertEqual("W", finder.current_direction)
        finder.turn_left()
        self.assertEqual("S", finder.current_direction)
        finder.turn_left()
        self.assertEqual("E", finder.current_direction)
        finder.turn_left()
        self.assertEqual("N", finder.current_direction)

    def test_incorrect_turn_direction_raises_error(self):
        finder = ShortestPathFinder("")
        self.assertRaises(ValueError, finder.apply_turn_move_instruction, "X1")

    def test_apply_turn_move_instruction(self):
        finder = ShortestPathFinder("")
        finder.apply_turn_move_instruction("R1")
        self.assertEqual(1, finder.moves_in_each_direction["E"])
        finder.apply_turn_move_instruction("L1")
        self.assertEqual(1, finder.moves_in_each_direction["N"])
        finder.apply_turn_move_instruction("L100")
        self.assertEqual(100, finder.moves_in_each_direction["W"])

##    def test_R2_L3(self):
##        test_input = "R2, L3"
##        finder = ShortestPathFinder(test_input)
##        self.assertEqual(5, finder.get_shortest_path_blocks())
##        
##    def test_R2_R2_R2(self):
##        test_input = "R2, R2, R2"
##        finder = ShortestPathFinder(test_input)
##        self.assertEqual(2, finder.get_shortest_path_blocks())
##
##    def test_R5_L5_R5_R3(self):
##        test_input = "R5, L5, R5, R3"
##        finder = ShortestPathFinder(test_input)
##        self.assertEqual(12, finder.get_shortest_path_blocks())

if __name__ == "__main__":
    unittest.main()
