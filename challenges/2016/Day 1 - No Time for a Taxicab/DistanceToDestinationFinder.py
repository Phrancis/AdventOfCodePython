from typing import Union, List, Tuple, Dict
from Coordinates import *


class DistanceToDestinationFinder:

    """
    Advent of Code - Day 1: No time for a Taxicab
    http://adventofcode.com/2016/day/1

    Solves the given problem, parts 1 & 2, in a quite literal implementation
    of taxicab geometry, deriving distances and positions based on movement
    in the 4 cardinal points.
    """
    
    CARDINALS_CLOCKWISE: List = ["N", "E", "S", "W"]
    last_instruction_index: int = 0
    current_direction: str = "N"
    moves_in_each_direction: Dict = {
        "N": 0,
        "E": 0,
        "S": 0,
        "W": 0
    }
    coordinates_history: List = []
    
    def __init__(self, raw_instructions: str) -> None:
        """
        Constructor.
        - Parses raw_instructions into a List
        - Adds starting position to coordinates_history list
        """
        self.instructions: List = raw_instructions.split(", ")
        self.coordinates_history.append(Coordinates(0, 0))

    def get_current_direction_index(self) -> int:
        """Return numeric index of current direction."""
        return self.CARDINALS_CLOCKWISE.index(self.current_direction)

    def get_nsew_values(self) -> Tuple:
        """Returns current North, South, East, West values"""
        north: int = self.moves_in_each_direction["N"]
        south: int = self.moves_in_each_direction["S"]
        east: int = self.moves_in_each_direction["E"]
        west: int = self.moves_in_each_direction["W"]
        return north, south, east, west

    def turn_right(self) -> None:
        """Sets current direction 90° to the right."""
        new_index: int = self.get_current_direction_index() + 1
        if new_index >= len(self.CARDINALS_CLOCKWISE):
            new_index = 0
        self.current_direction = self.CARDINALS_CLOCKWISE[new_index]

    def turn_left(self) -> None:
        """Sets current direction 90° to the left."""
        new_index: int = self.get_current_direction_index() - 1
        if new_index < 0:
            new_index = len(self.CARDINALS_CLOCKWISE) - 1
        self.current_direction = self.CARDINALS_CLOCKWISE[new_index]

    @staticmethod
    def get_turn_and_move_instructions(instruction: str) -> Tuple:
        """
        Takes a string like 'R1' or 'L200' and returns turn and move
        accordingly, e.g.: 'R1' = turn right and move 1 space, or ('R', 1).
        """
        turn: str = instruction[0].upper()
        moves: int = instruction[1:]
        if turn not in ["L", "R"]:
            raise ValueError(f"Invalid turn instruction: {turn}")
        try:
            moves = int(moves)
        except ValueError:
            raise ValueError(f"Invalid number of moves: {moves}")            
        return turn, moves

    def apply_turn_move_instruction(self, instruction: str) -> None:
        """Applies a turn and move instruction to state."""
        turn_move_instructions: Tuple = self.get_turn_and_move_instructions(instruction)
        turn: str = turn_move_instructions[0]
        moves: int = turn_move_instructions[1]
        if turn == "R":
            self.turn_right()
        elif turn == "L":
            self.turn_left()
        for i in range(moves):
            self.moves_in_each_direction[self.current_direction] += 1
            new_coordinates = self.get_current_coordinates()
            self.coordinates_history.append(new_coordinates)
        #     if self.coordinates_have_already_been_visited(new_coordinates):
        #         return self.get_first_index_of_coordinates(new_coordinates)
        # return index_of_first_instruction

    def get_first_index_of_coordinates(self, coordinates: "Coordinates") -> Union[int, None]:
        for coord in self.coordinates_history:
            if coord == coordinates:
                return self.coordinates_history.index(coord)
        return None

    def get_current_coordinates(self) -> Coordinates:
        """
        Calculates and returns the current position relative to the
        starting point.
        """
        north, south, east, west = self.get_nsew_values()
        latitude = north - south
        longitude = east - west
        return Coordinates(latitude, longitude)

    def coordinates_have_already_been_visited(self, other_coordinates: Coordinates) -> bool:
        """Returns whether a given position has already been visited."""
        for i in range(len(self.coordinates_history)):
            if self.coordinates_history[i] == other_coordinates \
               and not i == self.last_instruction_index:
                return True
        return False

    def get_shortest_path_from_input(self) -> int:
        """
        Solves Part 1 of the puzzle, which is finding the shortest distance
        with the entire input string regardless of locations. 
        """
        for instr in self.instructions:
            self.apply_turn_move_instruction(instr)
        north, south, east, west = self.get_nsew_values()
        latitude_movement = abs(north - south)
        longitude_movement = abs(east - west)
        return latitude_movement + longitude_movement

    def get_shortest_path_to_already_visited_location(self) -> int:

        new_instructions = []
        for i in range(len(self.instructions)):
            self.last_instruction_index = i
            self.apply_turn_move_instruction(self.instructions[i])
        return self.get_shortest_path_from_input()

    def get_human_friendly_coordinates_history(self) -> str:
        """Returns a human-friendly position history."""
        human_readable_coordinates_history = ""
        for i in range(len(self.coordinates_history)):
            human_readable_coordinates_history += f"position_id:{i}, coordinates:({str(self.coordinates_history[i])})\n"
        return human_readable_coordinates_history


if __name__ == "__main__":
    # puzzle_input = "R3, L2, L2, R4, L1, R2, R3, R4, L2, R4, L2, L5, L1, R5, R2, R2, L1, R4, R1, L5, L3, R4, R3, R1,
    #  L1, L5, L4, L2, R5, L3, L4, R3, R1, L3, R1, L3, R3, L4, R2, R5, L190, R2, L3, R47, R4, L3, R78, L1, R3, R190,
    # R4, L3, R4, R2, R5, R3, R4, R3, L1, L4, R3, L4, R1, L4, L5, R3, L3, L4, R1, R2, L4, L3, R3, R3, L2, L5, R1, L4,
    #  L1, R5, L5, R1, R5, L4, R2, L2, R1, L5, L4, R4, R4, R3, R2, R3, L1, R4, R5, L2, L5, L4, L1, R4, L4, R4, L4,
    # R1, R5, L1, R1, L5, R5, R1, R1, L3, L1, R4, L1, L4, L4, L3, R1, R4, R1, R1, R2, L5, L2, R4, L1, R3, L5, L2, R5,
    #  L4, R5, L5, R3, R4, L3, L3, L2, R2, L5, L5, R3, R4, R3, R4, R3, R1"
    puzzle_input = "R8, R4, R4, R8"
    finder = DistanceToDestinationFinder(puzzle_input)
    # print(finder.get_shortest_path_from_input())
    # print(finder.get_human_friendly_coordinates_history())
    print(finder.get_shortest_path_to_already_visited_location())
    print(finder.get_human_friendly_coordinates_history())
