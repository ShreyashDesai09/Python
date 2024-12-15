import requests

def get_api_data():
    get_url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(get_url)
    if response.status_code == 200:
        return True
        print(response.json())
    else:
        return False


print(get_api_data())