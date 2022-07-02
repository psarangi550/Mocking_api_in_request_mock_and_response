from mock import patch  # importing the patch decorator from the mock module
# from tests.mocking_mul_dependency_call import random_sum
from mocking_random.adv_mocktest.mocking_mul_dependency_call import random_sum
from mock import patch
import mock


@patch("mocking_random.adv_mocktest.mocking_mul_dependency_call.random")
def test_random_sum(mock_random):
    mock_random.randint.side_effect = [1, 2, 3]
    assert random_sum() == 3
