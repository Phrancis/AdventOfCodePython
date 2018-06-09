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

    def test_incorrect_number_of_moves_raises_error(self):
        finder = ShortestPathFinder("")
        self.assertRaises(ValueError, finder.apply_turn_move_instruction, "RX")

    def test_apply_turn_move_instruction(self):
        finder = ShortestPathFinder("")
        finder.apply_turn_move_instruction("R1")
        self.assertEqual(1, finder.moves_in_each_direction["E"])
        finder.apply_turn_move_instruction("L1")
        self.assertEqual(1, finder.moves_in_each_direction["N"])
        finder.apply_turn_move_instruction("L100")
        self.assertEqual(100, finder.moves_in_each_direction["W"])
        finder.apply_turn_move_instruction("L1000")
        self.assertEqual(1000, finder.moves_in_each_direction["S"])  

    def test_R2_L3(self):
        test_input = "R2, L3"
        finder = ShortestPathFinder(test_input)
        self.assertEqual(5, finder.get_shortest_path_blocks())
        
    def test_R2_R2_R2(self):
        test_input = "R2, R2, R2"
        finder = ShortestPathFinder(test_input)
        self.assertEqual(2, finder.get_shortest_path_blocks())

    def test_R5_L5_R5_R3(self):
        test_input = "R5, L5, R5, R3"
        finder = ShortestPathFinder(test_input)
        self.assertEqual(12, finder.get_shortest_path_blocks())

    def test_with_puzzle_input(self):
        test_input = "R3, L2, L2, R4, L1, R2, R3, R4, L2, R4, L2, L5, L1, R5, R2, R2, L1, R4, R1, L5, L3, R4, R3, R1, L1, L5, L4, L2, R5, L3, L4, R3, R1, L3, R1, L3, R3, L4, R2, R5, L190, R2, L3, R47, R4, L3, R78, L1, R3, R190, R4, L3, R4, R2, R5, R3, R4, R3, L1, L4, R3, L4, R1, L4, L5, R3, L3, L4, R1, R2, L4, L3, R3, R3, L2, L5, R1, L4, L1, R5, L5, R1, R5, L4, R2, L2, R1, L5, L4, R4, R4, R3, R2, R3, L1, R4, R5, L2, L5, L4, L1, R4, L4, R4, L4, R1, R5, L1, R1, L5, R5, R1, R1, L3, L1, R4, L1, L4, L4, L3, R1, R4, R1, R1, R2, L5, L2, R4, L1, R3, L5, L2, R5, L4, R5, L5, R3, R4, L3, L3, L2, R2, L5, L5, R3, R4, R3, R4, R3, R1"
        finder = ShortestPathFinder(test_input)
        self.assertEqual(262, finder.get_shortest_path_blocks())

if __name__ == "__main__":
    unittest.main()
