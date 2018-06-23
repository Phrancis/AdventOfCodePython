import unittest
from typing import List
from KeypadInstructionsInterpreter import *

class TestKeypadInstructionsInterpreter(unittest.TestCase):
    
    def test_attributes_are_the_correct_type(self):
        kii = KeypadInstructionsInterpreter("")
        self.assertIsInstance(kii.instructions_string, str)
        self.assertIsInstance(kii.KEYPAD, List)
        self.assertIsInstance(kii.instructions, List)
        self.assertIsInstance(kii.keypad_combination, List)
        

    def test_instructions_has_correct_contents(self):
        test_input = "ULL\nRRDDD\nLURDL\nUUUUD"
        expected_value = [
            ["U", "L", "L"],
            ["R", "R", "D", "D", "D"],
            ["L", "U", "R", "D", "L"],
            ["U", "U", "U", "U", "D"]
        ]
        kii = KeypadInstructionsInterpreter(test_input)
        self.assertEqual(expected_value, kii.instructions)
        

    def test_with_advent_of_code_example(self):
        test_input = "ULL\nRRDDD\nLURDL\nUUUUD"
        kii = KeypadInstructionsInterpreter(test_input)
        self.assertEqual(1985, kii.get_keypad_combination())

if __name__ == "__main__":
    unittest.main()
