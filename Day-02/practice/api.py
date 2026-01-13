import requests

url = "https://api.agify.io?name=meelad"

response = requests.get(url)

print(dir(response))

print(response.json())
