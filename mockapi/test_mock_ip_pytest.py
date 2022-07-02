from mock import patch
from unittest.mock import MagicMock
from mockapi.ip_fetch import get_ip
from mock import Mock

@patch("mockapi.ip_fetch.requests")
def test_get_ip(mock_request):
    mock_resp=Mock(status_code=200)
    mock_request.get.return_value = mock_resp
    mock_resp.raise_for_status.return_value = mock_resp.status_code
    mock_resp.json.return_value ={"origin":"1.1.1.1"}
    assert get_ip()=="1.1.1.1"

#alternate approach 

@patch("mockapi.ip_fetch.requests.get")
def test_req_get_ip(mock_request_get):
    mock_resp=mock_request_get()
    mock_resp.status_code = 200
    mock_resp.json.return_value ={"origin":"1.1.1.1"}
    assert get_ip()=="1.1.1.1"

#alternate approach 
@patch("mockapi.ip_fetch.requests.get")
def test_alter_get_ip(mock_req_get):
    kwargs={"name":"mock_resp","status_code":200,"json.return_value":{"origin":"1.1.1.1"}}
    mock_resp =MagicMock(**kwargs)
    mock_req_get.return_value=mock_resp
    assert get_ip()=="1.1.1.1"


