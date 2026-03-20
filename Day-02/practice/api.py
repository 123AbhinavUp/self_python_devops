import requests

url = "https://api.agify.io?name=meelad"

response = requests.get(url)

#print(dir(response))

print(response.json())

print(type(response.json()))

for key , value in response.json().items():
    if key == "abhinav":
        print(value)

