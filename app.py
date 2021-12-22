import requests

url = 'http://httpbin.org/status/200'
print(f"Checking {url}")
r = requests.get(url)
r.raise_for_status()
print("Check successful")
