import unittest
import responses
from mocking_responses import get_jokes
from responses import Response
from requests.exceptions import ConnectionError

class TestJokeExp(unittest.TestCase):
    
    @responses.activate
    def test_get_jokes_conn_exp(self):
        r=Response(
            method='GET',
            url="http://api.icndb.com/jokes/random",
            body=ConnectionError("Connection Error")
        )
        responses.add(r)
        self.assertEqual(get_jokes(),"Connection Error")

if __name__ == "__main__":
    unittest.main()
    
