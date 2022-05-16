import random
from anime_quote import anime
from inspiration_quote import motivate
from dogFact import dog

def main():
  instructions = 'Hello! Are you bored? sad? need some motivation? This program generates a quote from an anime, an inspiring quote, or an intersting dog fact that might make your day. Hope this makes you feel better!! Have fun!'
  print(instructions)
  print('1) Inspirational quote')
  print('2) Dog fact')
  print('3) Anime quote ^_^') 
  answer = int(input("Did you make a choice? Please enter the number:\n"))
 
  if answer == 1:
     print(motivate)
  elif answer == 2:
    print(dog)
  elif answer == 3:
    print(anime)
  else: 
     print("Please enter a number 1-3")

main()
