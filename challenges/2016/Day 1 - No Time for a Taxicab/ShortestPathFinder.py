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
        if len(instruction) == 2:
            moves = instruction[1]
        else:
            moves = instruction[1:len(instruction)-1]
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
        return
