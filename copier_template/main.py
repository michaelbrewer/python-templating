import requests
import json


if __name__ == "__main__":
    response = requests.get("https://httpbin.org/get")
    print(f"Response status code: {response.status_code}")
    print(json.dumps(response.json(), indent=4))
