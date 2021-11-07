import requests


def test_request():
    url = "https://httpbin.ceshiren.com/get"
    r = requests.get(url)
    print(r.status_code)
