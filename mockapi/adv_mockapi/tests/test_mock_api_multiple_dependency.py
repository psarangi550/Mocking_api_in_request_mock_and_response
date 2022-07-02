from mock import patch #importing the patch decorator
import mock #importing the mock module 
from mockapi.adv_mockapi.mocking_an_api_with_random_result import get_data


@patch("mockapi.adv_mockapi.mocking_an_api_with_random_result.requests.get")
@patch("mockapi.adv_mockapi.mocking_an_api_with_random_result.time.time")
@patch("mockapi.adv_mockapi.mocking_an_api_with_random_result.random.randint")
def test_get_data(mock_randint,mock_time,mock_request_get):
    result={
        "args":{
            "timestamp":12345678,
            "number":567
        }
    }
    mock_randint.return_value=result["args"]["number"]
    mock_time.return_value=result["args"]["timestamp"]
    mock_resp=mock.Mock(name="mock_response")
    mock_resp.status_code=200
    mock_resp.json.return_value=result
    mock_request_get.return_value=mock_resp

    assert get_data()==result["args"]


