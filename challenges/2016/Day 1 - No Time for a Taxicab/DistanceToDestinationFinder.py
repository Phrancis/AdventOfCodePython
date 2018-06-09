from Position import *

class DistanceToDestinationFinder:

    """
    Advent of Code - Day 1: No time for a Taxicab
    http://adventofcode.com/2016/day/1

    Solves the given problem, parts 1 & 2, in a quite literal implementation
    of taxicab geometry, deriving distances and positions based on movement
    in the 4 cardinal points.
    """
    
    CARDINALS_CLOCKWISE = ["N", "E", "S", "W"]
    
    def __init__(self, raw_directions:str) -> "DistanceToDestinationFinder":
        """
        Constructor.
        - Parses raw_directions into a List
        - Sets starting current_direction to North
        - Creates a Dict to log how many steps in each cardinal direction
          we have taken from the origin point
        - Creates empty position_history List
        - Adds starting position to position_history list
        """
        self.directions = raw_directions.split(", ")
        self.current_direction = "N"
        self.moves_in_each_direction = {
            "N" : 0,
            "E" : 0,
            "S" : 0,
            "W" : 0 }
        self.position_history = []
        self.position_history.append(Position(0,0))

    def get_current_direction_index(self) -> int:
        """Return numeric index of current direction."""
        return self.CARDINALS_CLOCKWISE.index(self.current_direction)

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

    def apply_turn_move_instruction(self, instruction:str) -> None:
        """
        Takes a string like 'R1' or 'L200' and updates state to turn and move
        accordingly, e.g., 'R1' = turn right and move 1 space.
        """
        turn = instruction[0].upper()
        moves = instruction[1:]
        try:
            moves = int(moves)
        except:
            raise ValueError(f"Invalid number of moves: {moves}")            
        if turn == "R":
            self.turn_right()
        elif turn == "L":
            self.turn_left()
        else:
            raise ValueError(f"Invalid turn instruction: {turn}")
        self.moves_in_each_direction[self.current_direction] += moves
        self.position_history.append(self.get_current_position())

    def get_current_position(self) -> "Position":
        """
        Calculates and returns the current position relative to the
        starting point.
        """
        north = self.moves_in_each_direction["N"]
        south = self.moves_in_each_direction["S"]
        east = self.moves_in_each_direction["E"]
        west = self.moves_in_each_direction["W"]
        latitude = north - south
        longitude = east - west
        return Position(latitude, longitude)

    def position_has_already_been_visited(self, other_position:"Position") -> bool:
        """Returns whether a given position has already been visited."""
        for position in self.position_history:
            if position == other_position:
                return True
        return False

    def get_shortest_path_from_input(self) -> int:
        """
        Solves Part 1 of the puzzle, which is finding the shortest distance
        with the entire input string regardless of locations. 
        """
        for instruction in self.directions:
            self.apply_turn_move_instruction(instruction)            
        north = self.moves_in_each_direction["N"]
        south = self.moves_in_each_direction["S"]
        east = self.moves_in_each_direction["E"]
        west = self.moves_in_each_direction["W"]
        latitude_movement = abs(north - south)
        longitude_movement = abs(east - west)
        return latitude_movement + longitude_movement

    def get_human_friendly_position_history(self) -> str:
        """Returns a human-friendly position history."""
        human_readable_position_history = ""
        for i in range(len(self.position_history)):
            human_readable_position_history += f"position_id:{i}, position:({str(self.position_history[i])})\n"
        return human_readable_position_history

if __name__ == "__main__":
    puzzle_input = "R3, L2, L2, R4, L1, R2, R3, R4, L2, R4, L2, L5, L1, R5, R2, R2, L1, R4, R1, L5, L3, R4, R3, R1, L1, L5, L4, L2, R5, L3, L4, R3, R1, L3, R1, L3, R3, L4, R2, R5, L190, R2, L3, R47, R4, L3, R78, L1, R3, R190, R4, L3, R4, R2, R5, R3, R4, R3, L1, L4, R3, L4, R1, L4, L5, R3, L3, L4, R1, R2, L4, L3, R3, R3, L2, L5, R1, L4, L1, R5, L5, R1, R5, L4, R2, L2, R1, L5, L4, R4, R4, R3, R2, R3, L1, R4, R5, L2, L5, L4, L1, R4, L4, R4, L4, R1, R5, L1, R1, L5, R5, R1, R1, L3, L1, R4, L1, L4, L4, L3, R1, R4, R1, R1, R2, L5, L2, R4, L1, R3, L5, L2, R5, L4, R5, L5, R3, R4, L3, L3, L2, R2, L5, L5, R3, R4, R3, R4, R3, R1"
    finder = DistanceToDestinationFinder(puzzle_input)
    print(finder.get_shortest_path_from_input())
    print(finder.get_human_friendly_position_history())
