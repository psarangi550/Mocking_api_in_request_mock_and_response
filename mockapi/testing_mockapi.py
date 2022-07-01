from mock import Mock #importing the mock class from mock module
import mock #importing the mock module  
import unittest#importing the unittest module 
from mock_api import len_jokes,get_jokes
from mock import MagicMock #importing the MagicMock class from the mock module
from mock import patch #importing the patch class from the mock module
import requests.exceptions #importing the request.exceptions

class TestLenJokes(unittest.TestCase):

    def test_len_jokes(self):
        len_jokes = mock.Mock(return_value=3)
        self.assertEqual(len_jokes(),3)

    # alternate approach is below
    @patch('mock_api.get_jokes')
    def test_len_jokes_alter(self,mock_get_jokes):
        mock_get_jokes.return_value ="one"
        self.assertEqual(len_jokes(),3)
    
    #mocking the request module for the get_jokes method
    @patch('mock_api.requests') # mocking the request library for the get_jokes method
    def test_get_jokes(self,mock_request):
        mock_response=MagicMock(status_code=200)
        mock_request.get.return_value = mock_response
        mock_response.json.return_value = {"value":{"joke":"Hello"}}
        self.assertEqual(get_jokes(),"Hello")
    
    #here using the exception to check the side_effects
    @patch('mock_api.requests') #mocking the request Api 
    def test_get_jokes_time_exp(self, mock_request):
        mock_request.exceptions=requests.exceptions
        mock_response=MagicMock(status_code=403)
        mock_request.get.side_effect = requests.exceptions.Timeout('something went wrong')
        self.assertEqual(get_jokes(),"Timeout")
    
    # here i am also using the exception to test that connection error also gives us the same thing
    @patch('mock_api.requests') #mocking the request Api 
    def test_get_jokes_conn_exp(self, mock_request):
        mock_request.exceptions=requests.exceptions
        mock_response=MagicMock(status_code=403)
        mock_request.get.side_effect = requests.exceptions.ConnectionError('something went wrong')
        self.assertEqual(get_jokes(),"Connection Error")
    
    @patch('mock_api.requests') #mocking the request Api 
    def test_get_jokes_http_exp(self, mock_request):
        mock_request.exceptions=requests.exceptions
        mock_response=MagicMock(status_code=503)
        mock_request.get.return_value=mock_response
        mock_response.raise_for_status.side_effect=requests.exceptions.HTTPError('something went wrong')
        self.assertEqual(get_jokes(),"HTTPError")
    
    #fetching the authentication error from HTTPError
    @patch('mock_api.requests') #mocking the request Api 
    def test_get_jokes_http_auth_exp(self, mock_request):
        mock_request.exceptions=requests.exceptions
        mock_response=MagicMock()
        mock_response.status_code=403
        mock_request.get.return_value=mock_response
        mock_response.raise_for_status.side_effect=requests.exceptions.HTTPError('something went wrong')
        mock_response.raise_for_status.side_effect.response=mock_response.status_code
        self.assertEqual(get_jokes(),"Authentication Error")


if __name__ == "__main__":
    unittest.main()





