import requests
import json
post_data={
    "title": "My first blogpost ever!", 
    "body": "Lorem ipsum dolor sit amet.", 
    "author": "Elke"
    }

headers={
    "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}


def get_data():
    resp=requests.get("http://localhost:8001/")
    return (resp.text)

def send_post_req():
    resp=requests.post("http://localhost:8001",data=json.dumps(post_data))
    return (resp.text)

if __name__ == "__main__":
    # print(get_data())
    print(send_post_req())
