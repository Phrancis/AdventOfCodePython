from typing import List, Tuple
from Coordinates import *

class DistanceToDestinationFinder:

    """
    Advent of Code - Day 1: No time for a Taxicab
    http://adventofcode.com/2016/day/1

    Solves the given problem, parts 1 & 2, in a quite literal implementation
    of taxicab geometry, deriving distances and positions based on movement
    in the 4 cardinal points.
    """
    
    CARDINALS_CLOCKWISE = ["N", "E", "S", "W"]
    
    def __init__(self, raw_instructions:str) -> "DistanceToDestinationFinder":
        """
        Constructor.
        - Parses raw_instructions into a List
        - Declares a last_instruction_index to keep track of where we are in
          the list of directions
        - Sets starting current_direction to North
        - Declares a Dict to log how many steps in each cardinal direction
          we have taken from the origin point
        - Declares an empty coordinates_history List
        - Adds starting position to coordinates_history list
        """
        self.instructions = raw_instructions.split(", ")
        self.last_instruction_index = 0
        self.current_direction = "N"
        self.moves_in_each_direction = {
            "N" : 0,
            "E" : 0,
            "S" : 0,
            "W" : 0 }
        self.coordinates_history = []
        self.coordinates_history.append(Coordinates(0,0))

    def get_current_direction_index(self) -> int:
        """Return numeric index of current direction."""
        return self.CARDINALS_CLOCKWISE.index(self.current_direction)

    def get_NSEW_values(self) -> Tuple:
        """Returns current North, South, East, West values"""
        north = self.moves_in_each_direction["N"]
        south = self.moves_in_each_direction["S"]
        east = self.moves_in_each_direction["E"]
        west = self.moves_in_each_direction["W"]
        return north, south, east, west

    def turn_right(self) -> None:
        """Sets current direction 90° to the right."""
        new_index = self.get_current_direction_index() + 1
        if new_index >= len(self.CARDINALS_CLOCKWISE):
            new_index = 0
        self.current_direction = self.CARDINALS_CLOCKWISE[new_index]

    def turn_left(self) -> None:
        """Sets current direction 90° to the left."""
        new_index = self.get_current_direction_index() - 1
        if new_index < 0:
            new_index = len(self.CARDINALS_CLOCKWISE) - 1
        self.current_direction = self.CARDINALS_CLOCKWISE[new_index]

    def get_turn_and_move_instructions(self, instruction:str) -> Tuple:
        """
        Takes a string like 'R1' or 'L200' and returns turn and move
        accordingly, e.g., 'R1' = turn right and move 1 space, or ('R', 1).
        """
        turn = instruction[0].upper()
        moves = instruction[1:]
        if turn != "L" and turn != "R":
            raise ValueError(f"Invalid turn instruction: {turn}")
        try:
            moves = int(moves)
        except:
            raise ValueError(f"Invalid number of moves: {moves}")            
        return turn, moves

    def apply_turn_move_instruction(self, instruction:str) -> bool:
        """Applies a turn and move instruction to state."""
        turn, moves = self.get_turn_and_move_instructions(instruction)
        if turn == "R":
            self.turn_right()
        elif turn == "L":
            self.turn_left()
        for i in range(moves):
            self.moves_in_each_direction[self.current_direction] += 1
            new_coordinates = self.get_current_coordinates()
            self.coordinates_history.append(new_coordinates)
##            if self.coordinates_have_already_been_visited(new_coordinates):
##                return True
##        return False

    def get_current_coordinates(self) -> "Coordinates":
        """
        Calculates and returns the current position relative to the
        starting point.
        """
        north, south, east, west = self.get_NSEW_values()
        latitude = north - south
        longitude = east - west
        return Coordinates(latitude, longitude)

    def coordinates_have_already_been_visited(self, other_coordinates:"Coordinates") -> bool:
        """Returns whether a given position has already been visited."""
        for i in range(len(self.coordinates_history)):
            if self.coordinates_history[i] == other_coordinates \
               and not i == self.last_instruction_index:
                return True
        return False

    def get_shortest_path_from_input(self, instructions:List=[]) -> int:
        """
        Solves Part 1 of the puzzle, which is finding the shortest distance
        with the entire input string regardless of locations. 
        """
        if instructions == []:
            instructions = self.instructions
        for instruction in instructions:
            self.apply_turn_move_instruction(instruction)            
        north, south, east, west = self.get_NSEW_values()
        latitude_movement = abs(north - south)
        longitude_movement = abs(east - west)
        return latitude_movement + longitude_movement

    def get_shortest_path_to_already_visited_location(self) -> int:
        
        for i in range(len(self.instructions)):
            self.last_instruction_index = i
            self.apply_turn_move_instruction(self.instructions[i])
            new_instructions = []
            ## THERE IS SOMETHING DEEPLY WRONG
            if self.coordinates_have_already_been_visited(self.coordinates_history[-1]):
                new_instructions = self.instructions[0:self.last_instruction_index]
                break
        return self.get_shortest_path_from_input(new_instructions)
            

    def get_human_friendly_coordinates_history(self) -> str:
        """Returns a human-friendly position history."""
        human_readable_coordinates_history = ""
        for i in range(len(self.coordinates_history)):
            human_readable_coordinates_history += f"position_id:{i}, coordinates:({str(self.coordinates_history[i])})\n"
        return human_readable_coordinates_history

if __name__ == "__main__":
    #puzzle_input = "R3, L2, L2, R4, L1, R2, R3, R4, L2, R4, L2, L5, L1, R5, R2, R2, L1, R4, R1, L5, L3, R4, R3, R1, L1, L5, L4, L2, R5, L3, L4, R3, R1, L3, R1, L3, R3, L4, R2, R5, L190, R2, L3, R47, R4, L3, R78, L1, R3, R190, R4, L3, R4, R2, R5, R3, R4, R3, L1, L4, R3, L4, R1, L4, L5, R3, L3, L4, R1, R2, L4, L3, R3, R3, L2, L5, R1, L4, L1, R5, L5, R1, R5, L4, R2, L2, R1, L5, L4, R4, R4, R3, R2, R3, L1, R4, R5, L2, L5, L4, L1, R4, L4, R4, L4, R1, R5, L1, R1, L5, R5, R1, R1, L3, L1, R4, L1, L4, L4, L3, R1, R4, R1, R1, R2, L5, L2, R4, L1, R3, L5, L2, R5, L4, R5, L5, R3, R4, L3, L3, L2, R2, L5, L5, R3, R4, R3, R4, R3, R1"
    puzzle_input = "R8, R4, R4, R8"
    finder = DistanceToDestinationFinder(puzzle_input)
    #print(finder.get_shortest_path_from_input())
    #print(finder.get_human_friendly_coordinates_history())
    print(finder.get_shortest_path_to_already_visited_location())
    print(finder.get_human_friendly_coordinates_history())
