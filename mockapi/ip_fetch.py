import requests

def get_ip():
    try:
        response = requests.get("https://httpbin.org/ip",timeout=30)
        response.raise_for_status()
    except requests.exceptions.Timeout:
        return "Timeout Exception"
    except requests.exceptions.ConnectionError:
        return "Connection Error"
    except requests.exceptions.HTTPError:
        return "HTTPError"
    else:
        if response.status_code == 200:
            return response.json()["origin"]
        else:
            return "No IP found"

# if __name__=="__main__":
#     print(get_ip())