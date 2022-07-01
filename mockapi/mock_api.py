import requests

def len_jokes():
    jokes=get_jokes()
    return len(jokes)


def get_jokes():
    try:
        response=requests.get("http://api.icndb.com/jokes/random",timeout=30)
        response.raise_for_status()
    except requests.exceptions.Timeout:
        return "Timeout"
    except requests.exceptions.ConnectionError:
        return "Connection Error"
    except requests.exceptions.HTTPError as e:
        # return "Http Error"
        if e.response == 403:
            return "Authentication Error"
        else:
            return "HTTPError"
    else:
        if response.status_code==200:
                joke=response.json()['value']['joke']
        else:
            joke="No jokes found"
        return joke

# print(len_jokes())