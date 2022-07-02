from mock import patch
import pytest
from mocking_random.guessing_number_rolling_dice import guess_number,roll_dice


# @patch("mocking_random.guessing_number_rolling_dice.roll_dice")
# def test_get_jokes(mock_roll_dice):
#     mock_roll_dice.return_value = 3
#     assert guess_number(3) == "You Won"
#     assert guess_number(4) == "You Lost"

# parameterizing the test function 
@pytest.mark.parametrize("nums",[3,4,5])
@patch("mocking_random.guessing_number_rolling_dice.roll_dice")
def test_get_jokes_param(mock_roll_dice,nums):
    mock_roll_dice.return_value = 3
    assert guess_number(nums) == "You Won"
    mock_roll_dice.assert_called()


# @pytest.mark.parametrize("nums",[2,3,4])
# def test_param(nums):
#     assert type(nums)==int