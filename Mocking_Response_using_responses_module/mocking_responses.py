import requests

def len_jokes():
    jokes=get_jokes()
    return len(jokes)

def get_jokes():
    try:
        resp=requests.get("http://api.icndb.com/jokes/random",timeout=30)
        resp.raise_for_status()
    except requests.exceptions.Timeout:
        return "Request Time Out"
    except requests.exceptions.ConnectionError:
        return "Connection Error"
    except requests.exceptions.HTTPError:
        return "Something went wrong"
    else:
        if resp.status_code==200:
            jokes=resp.json()['value']['joke']
        else:
            jokes="No Jokes"
    return jokes



if __name__ == "__main__":
    print(get_jokes())
    print(len_jokes())