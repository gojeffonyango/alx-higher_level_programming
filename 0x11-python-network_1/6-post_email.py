#!bin/bash/python3

if __name__ == '__main__':
    import sys
    import requests

    url = sys.argv[1]
    email = sys.argv[2]
    response = requests.post(url, data={'email': email})
    print(response.text)
