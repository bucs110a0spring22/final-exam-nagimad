import requests

response = requests.get('https://x-math.herokuapp.com/api/random?max=99&min=1')
   
number=response.json()["answer"]
print(f'Your number is: {number}\n')