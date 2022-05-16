import requests

response = requests.get('http://dog-api.kinduff.com/api/facts')

dog = response.json()