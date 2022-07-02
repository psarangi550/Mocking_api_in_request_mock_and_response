from guessing_number_rolling_dice import guess_number,roll_dice
#import guessing_number and roll_dice method from the respective module 
from unittest.mock import patch
import random #importing the random module
import unittest #importing the unittest module
from mock import Mock

class TestGuess(unittest.TestCase):
    
    @patch("guessing_number_rolling_dice.roll_dice")
    def test_guess(self,mock_roll_dice):
        mock_roll_dice.return_value = 3
        self.assertEqual(guess_number(3),"You Won")

    #alternate approach to test
    def test_alter_guess(self):
        mock_roll_dice=Mock()
        mock_roll_dice.return_value = 3
        self.assertEqual(guess_number(3),"You Won")

    #alternate to mock roll_dice
    def test_guess_alter(self):
        mock_roll_dice=Mock()
        roll_dice=mock_roll_dice
        mock_roll_dice.return_value=4
        self.assertEqual(guess_number(3),"You Lost")




if __name__ == "__main__":
    unittest.main()