import requests
import json

def main():
    url = 'http://127.0.0.1:8000/'
    data = {
        'x': 3,
        'y': 4
    }
    res = requests.post(url, json.dumps(data))
    print(res.json())

if __name__ == '__main__':
    main()