import requests
import random
import json
import time

def get_data():
    params={
        "timestamp": time.time(),
        "number":random.randint(1,100)
    }
    resp=requests.get("https://httpbin.org/get",params=params)
    if resp.status_code == 200:
        return resp.json()["args"]
    else:
        return "something went wrong"


if __name__=="__main__":
    print(get_data())