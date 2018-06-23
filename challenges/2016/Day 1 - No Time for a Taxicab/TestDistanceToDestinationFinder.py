import unittest
from DistanceToDestinationFinder import *
from Coordinates import *


class TestDistanceToDestinationFinder(unittest.TestCase):
    def test_instructions_are_converted_to_list(self) -> None:
        test_input: str = "R5, L5, R5, R3"
        finder1 = DistanceToDestinationFinder(test_input)
        self.assertIsInstance(finder1.instructions, List)
        self.assertEqual(4, len(finder1.instructions))

    def test_facing_north_initially(self) -> None:
        finder2 = DistanceToDestinationFinder("")
        self.assertEqual("N", finder2.current_direction)

    def test_initial_position_is_correct(self) -> None:
        finder3 = DistanceToDestinationFinder("")
        self.assertEqual(Coordinates(0,0), finder3.coordinates_history[0])

    def test_get_current_direction_index_for_all_cardinals(self) -> None:
        finder4 = DistanceToDestinationFinder("")
        self.assertEqual(0, finder4.get_current_direction_index())
        finder4.current_direction = "E"
        self.assertEqual(1, finder4.get_current_direction_index())
        finder4.current_direction = "S"
        self.assertEqual(2, finder4.get_current_direction_index())
        finder4.current_direction = "W"
        self.assertEqual(3, finder4.get_current_direction_index())

    def test_turn_right(self) -> None:
        finder5 = DistanceToDestinationFinder("")
        finder5.turn_right()
        self.assertEqual("E", finder5.current_direction)
        finder5.turn_right()
        self.assertEqual("S", finder5.current_direction)
        finder5.turn_right()
        self.assertEqual("W", finder5.current_direction)
        finder5.turn_right()
        self.assertEqual("N", finder5.current_direction)

    def test_turn_left(self) -> None:
        finder6 = DistanceToDestinationFinder("")
        finder6.turn_left()
        self.assertEqual("W", finder6.current_direction)
        finder6.turn_left()
        self.assertEqual("S", finder6.current_direction)
        finder6.turn_left()
        self.assertEqual("E", finder6.current_direction)
        finder6.turn_left()
        self.assertEqual("N", finder6.current_direction)

    def test_incorrect_turn_direction_raises_error(self) -> None:
        finder7 = DistanceToDestinationFinder("")
        self.assertRaises(ValueError, finder7.apply_turn_move_instruction, "X1")

    def test_incorrect_number_of_moves_raises_error(self) -> None:
        finder8 = DistanceToDestinationFinder("")
        self.assertRaises(ValueError, finder8.apply_turn_move_instruction, "RX")

    def test_apply_turn_move_instruction(self) -> None:
        finder9 = DistanceToDestinationFinder("")
        finder9.apply_turn_move_instruction("R1")
        self.assertEqual(1, finder9.moves_in_each_direction["E"])
        finder9.apply_turn_move_instruction("L1")
        self.assertEqual(1, finder9.moves_in_each_direction["N"])
        finder9.apply_turn_move_instruction("L100")
        self.assertEqual(100, finder9.moves_in_each_direction["W"])
        finder9.apply_turn_move_instruction("L1000")
        self.assertEqual(1000, finder9.moves_in_each_direction["S"])

    def test_get_current_coordinates(self) -> None:
        finder10 = DistanceToDestinationFinder("")
        self.assertEqual(Coordinates(0,0), finder10.get_current_coordinates())
        finder10.apply_turn_move_instruction("R1")
        self.assertEqual(Coordinates(0,1), finder10.get_current_coordinates())
        finder10.apply_turn_move_instruction("R1")
        self.assertEqual(Coordinates(-1,1), finder10.get_current_coordinates())
        finder10.apply_turn_move_instruction("R1")
        self.assertEqual(Coordinates(-1,0), finder10.get_current_coordinates())
        finder10.apply_turn_move_instruction("R1")
        self.assertEqual(Coordinates(0,0), finder10.get_current_coordinates())

    def test_coordinates_have_already_been_visited(self) -> None:
        finder11 = DistanceToDestinationFinder("")
        finder11.coordinates_history.append(Coordinates(1,1))
        finder11.coordinates_history.append(Coordinates(2,2))
        self.assertTrue(finder11.coordinates_have_already_been_visited(Coordinates(1,1)))

    def test_part1_R2_L3(self) -> None:
        test_input = "R2, L3"
        finder12 = DistanceToDestinationFinder(test_input)
        self.assertEqual(5, finder12.get_shortest_path_from_input())
        
    def test_part1_R2_R2_R2(self) -> None:
        test_input = "R2, R2, R2"
        finder13 = DistanceToDestinationFinder(test_input)
        self.assertEqual(2, finder13.get_shortest_path_from_input())

    def test_part1_R5_L5_R5_R3(self) -> None:
        test_input = "R5, L5, R5, R3"
        finder14 = DistanceToDestinationFinder(test_input)
        self.assertEqual(12, finder14.get_shortest_path_from_input())

    def test_part1_with_puzzle_input(self) -> None:
        test_input = "R3, L2, L2, R4, L1, R2, R3, R4, L2, R4, L2, L5, L1, R5, R2, R2, L1, R4, R1, L5, L3, R4, R3, R1, "\
                     "L1, L5, L4, L2, R5, L3, L4, R3, R1, L3, R1, L3, R3, L4, R2, R5, L190, R2, L3, R47, R4, L3, R78, "\
                     "L1, R3, R190, R4, L3, R4, R2, R5, R3, R4, R3, L1, L4, R3, L4, R1, L4, L5, R3, L3, L4, R1, R2, "\
                     "L4, L3, R3, R3, L2, L5, R1, L4, L1, R5, L5, R1, R5, L4, R2, L2, R1, L5, L4, R4, R4, R3, R2, R3, "\
                     "L1, R4, R5, L2, L5, L4, L1, R4, L4, R4, L4, R1, R5, L1, R1, L5, R5, R1, R1, L3, L1, R4, L1, L4, "\
                     "L4, L3, R1, R4, R1, R1, R2, L5, L2, R4, L1, R3, L5, L2, R5, L4, R5, L5, R3, R4, L3, L3, L2, R2, "\
                     "L5, L5, R3, R4, R3, R4, R3, R1 "
        finder15 = DistanceToDestinationFinder(test_input)
        self.assertEqual(262, finder15.get_shortest_path_from_input())

    def test_part2_R8_R4_R4_R8(self) -> None:
        test_input = "R8, R4, R4, R8"
        finder16 = DistanceToDestinationFinder(test_input)
        self.assertEqual(4, finder16.get_shortest_path_to_already_visited_location())


if __name__ == "__main__":
    unittest.main()
