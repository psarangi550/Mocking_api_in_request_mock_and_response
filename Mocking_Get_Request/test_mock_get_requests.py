import requests
import unittest
import requests_mock

def len_jokes():
    jokes=get_jokes()
    return len(jokes)



def get_jokes()->str:
    resp=requests.get("http://api.icndb.com/jokes/random")
    if resp.status_code == 200:
        jokes=resp.json()['value']['joke']
    else:
        jokes="No Jokes"
    return jokes



@requests_mock.Mocker()
class TestJokes(unittest.TestCase):
    
    #mocking the len_jokes method
    def test_len_jokes(self,get_jokes):
        get_jokes.register_uri("GET",url="http://api.icndb.com/jokes/random",status_code=200,json={"value":{"joke":"Hello"}})
        self.assertEqual(len_jokes(),5)
        
    #mocking the get_jokes method 
    def test_get_jokes(self,mock):
        mock.register_uri("GET",url="http://api.icndb.com/jokes/random",status_code=200,json={"value":{"joke":"Hello"}})
        self.assertEqual(get_jokes(),"Hello")


        
if __name__ == "__main":
    unittest.main()


        
    
