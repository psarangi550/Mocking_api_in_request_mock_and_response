from mocking_random.guessing_number_rolling_dice import guess_number,roll_dice
import mock #importing the mock module
from mock import patch #importing the patch decorator
import pytest

@pytest.fixture(scope="function")
def mock_roll_fixture():
    with patch("mocking_random.guessing_number_rolling_dice.roll_dice") as mock_roll_dice:
        return mock_roll_dice
    
def test_guess_num(mock_roll_fixture):
    mock_roll_fixture.return_value=3
    assert guess_number(3)=="You Won"

