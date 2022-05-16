import requests

response = requests.get('https://api.goprogram.ai/inspiration')

motivate = response.json()
