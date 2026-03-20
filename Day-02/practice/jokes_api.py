import requests


joke_api = "https://official-joke-api.appspot.com/random_joke"

data = requests.get(joke_api)

print(dir(data))

if data.status_code == 200:

    joke_data = data.json()

    print(joke_data)
else:
    print(f"Failed to fetch joke. Status code: {data.status_code}")