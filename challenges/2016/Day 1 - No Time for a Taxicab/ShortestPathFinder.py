# Advent of Code - Day 1: No time for a Taxicab
# http://adventofcode.com/2016/day/1

class ShortestPathFinder:
    CARDINALS_CLOCKWISE = ["N", "E", "S", "W"]
    
    def __init__(self, raw_directions:str) -> None:
        self.directions = raw_directions.split(", ")
        self.current_direction = "N"
        self.moves_in_each_direction = {
            "N" : 0,
            "E" : 0,
            "S" : 0,
            "W" : 0 }

    def get_current_index(self) -> int:
        return self.CARDINALS_CLOCKWISE.index(self.current_direction)

    def turn_right(self) -> None:
        new_index = self.get_current_index() + 1
        if new_index >= len(self.CARDINALS_CLOCKWISE):
            new_index = 0
        self.current_direction = self.CARDINALS_CLOCKWISE[new_index]

    def turn_left(self) -> None:
        new_index = self.get_current_index() - 1
        if new_index < 0:
            new_index = len(self.CARDINALS_CLOCKWISE) - 1
        self.current_direction = self.CARDINALS_CLOCKWISE[new_index]

    def apply_turn_move_instruction(self, instruction:str) -> None:
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

    def get_shortest_path_blocks(self) -> int:
        for instruction in self.directions:
            self.apply_turn_move_instruction(instruction)            
        north = self.moves_in_each_direction["N"]
        south = self.moves_in_each_direction["S"]
        east = self.moves_in_each_direction["E"]
        west = self.moves_in_each_direction["W"]
        latitude_movement = abs(north - south)
        longitude_movement = abs(east - west)
        return latitude_movement + longitude_movement

if __name__ == "__main__":
    puzzle_input = "R3, L2, L2, R4, L1, R2, R3, R4, L2, R4, L2, L5, L1, R5, R2, R2, L1, R4, R1, L5, L3, R4, R3, R1, L1, L5, L4, L2, R5, L3, L4, R3, R1, L3, R1, L3, R3, L4, R2, R5, L190, R2, L3, R47, R4, L3, R78, L1, R3, R190, R4, L3, R4, R2, R5, R3, R4, R3, L1, L4, R3, L4, R1, L4, L5, R3, L3, L4, R1, R2, L4, L3, R3, R3, L2, L5, R1, L4, L1, R5, L5, R1, R5, L4, R2, L2, R1, L5, L4, R4, R4, R3, R2, R3, L1, R4, R5, L2, L5, L4, L1, R4, L4, R4, L4, R1, R5, L1, R1, L5, R5, R1, R1, L3, L1, R4, L1, L4, L4, L3, R1, R4, R1, R1, R2, L5, L2, R4, L1, R3, L5, L2, R5, L4, R5, L5, R3, R4, L3, L3, L2, R2, L5, L5, R3, R4, R3, R4, R3, R1"
    shortest_path_finder = ShortestPathFinder(puzzle_input)
    print(shortest_path_finder.moves_in_each_direction)
    print(shortest_path_finder.get_shortest_path_blocks())
