import responses
import unittest
from mocking_responses import get_jokes
from responses import Response

class TestJokes(unittest.TestCase):
    
    #mocking the get request using the resposes.get
    @responses.activate
    def test_get_jokes(self):
        responses.get(
            url="http://api.icndb.com/jokes/random",
            status=200,
            json={"value":{"joke":"Hello"}}
        )
        self.assertEqual(get_jokes(),"Hello")
    
    #alternate way of handling using the Response class of the responses module in python 
    
    @responses.activate
    def test_get_joke_alter(self):
        r=Response(
            method="GET",
            url="http://api.icndb.com/jokes/random",
            status=200,
            json={"value":{"joke":"Hello"}}
            )
        responses.add(r)
        self.assertEqual(get_jokes(),"Hello")
    
    #handling the 404 Execption
    @responses.activate
    def test_get_jokes_exp(self):
        responses.get(
            url="http://api.icndb.com/jokes/random",
            status=404,
            json={"value":{"joke":"Hello"}}
        )
        self.assertEqual(get_jokes(),"Something went wrong")
    
    #handling the same response using the alternate way
    @responses.activate
    def test_get_jokes_exp_alter(self):
        r=Response(
            method="GET",
            url="http://api.icndb.com/jokes/random",
            status=404,
            json={"value":{"joke":"Hello"}}
        )
        responses.add(r)
        self.assertEqual(get_jokes(),"Something went wrong")
    
    
    
if __name__ == "__main__":
    unittest.main()


