import requests
import unittest
import requests_mock

def len_jokes():
    jokes=get_jokes()
    return len(jokes)



def get_jokes()->str:
    resp=requests.get("http://api.icndb.com/jokes/random")
    print(resp)
    if resp.status_code == 200:
        jokes=resp.json()['value']['joke']
    else:
        jokes="No Jokes"
    return jokes


@requests_mock.Mocker()
class TestJokesExp(unittest.TestCase):
    
    #mocking the 404 Error in case of get_jokes
    def test_get_exp(self,mock):
        mock.register_uri("GET",url="http://api.icndb.com/jokes/random",status_code=404,json={"value":{"joke":"Hello"}})
        self.assertEqual(get_jokes(),"No Jokes")
    
    #mocking the 404 error in case of the len_joke function output
    def test_len_exp(self,get_jokes):
        get_jokes.register_uri("GET",url="http://api.icndb.com/jokes/random",status_code=404,json={"value":{"joke":"Hello"}})
        self.assertEqual(len_jokes(),8)
        
        
if __name__ == "__main":
    unittest.main()


        
    
