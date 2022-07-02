from mock import patch  # importing the patch decorator from the mock module
# from tests.mocking_mul_dependency_call import random_sum
from mocking_random.adv_mocktest.mocking_mul_dependency_call import random_sum
from mock import patch
import mock


@patch("mocking_random.adv_mocktest.mocking_mul_dependency_call.random")
def test_random_sum(mock_random):
    mock_random.randint.side_effect = [1, 2, 3]
    assert random_sum() == 3

#alternate approach to perform the same  test 
@patch("mocking_random.adv_mocktest.mocking_mul_dependency_call.random.randint")
def test_random_sum_alter(mock_random_randint):
    mock_random_randint.side_effect = [1, 2, 3]
    assert random_sum() == 3
    mock_random_randint.assert_called_with(1,100)
