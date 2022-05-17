#import random
from anime_quote import anime
from dogFact import dog
from math_number import number

def main():
  instructions = 'Hello! This program generates a number, which is an answer to a random math equation. It then uses that number to generate either an anime quote or a dog fact. Have fun!'
  print(instructions)

  answer = int(input("Please enter your number from above: \n"))
 
  if answer <= 50:
     print(anime)
  elif answer >= 51:
    print(dog)
    
  else:
    print("please enter your number")

main()