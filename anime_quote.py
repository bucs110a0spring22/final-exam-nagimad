import requests

response = requests.get("https://animechan.vercel.app/api/random")

anime = response.json()
