from typing import List

class KeypadInstructionsInterpreter:
    KEYPAD = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    instructions = []
    keypad_combination = []

    def __init__(self, instructions_string:str) -> "KeypadInstructionsInterpreter":
        self.instructions_string = instructions_string
        self.parse_instructions(instructions_string)

    def parse_instructions(self, instructions_string:str) -> List:
        digit_directions = instructions_string.split("\n")
        for direction in digit_directions:
            self.instructions.append(list(direction))

    def interpret_instruction(self, instruction:str) -> None:
        return

    def get_keypad_combination(self) -> None:
        return
            
if __name__ == "__main__":
    test_input = test_input = "ULL\nRRDDD\nLURDL\nUUUUD"
    kii = KeypadInstructionsInterpreter(test_input)
    print(kii.instructions)
