# Comment 

import random
from secrets import choice 


myInteger = 5

print(type(myInteger))

myInteger = '3'

print(int(myInteger))

print('Value: ' + (myInteger))


def getGameResult():
    options = ["scissors","rock","paper"]
    currentChoice = options[random.randint(0, len(options) -1)]
    print(f"I choose: {currentChoice}")

myValue = input("What are you? ")
print('Your answer : ' + (myValue))
print(f"Hi {myValue}, I am python" )
print(f"{myValue}, we can play Rock Paper Scissors")
attack = input(f"{myValue}, Choose something  ").lower()
print(f"Your choice is: {attack}")
if attack != "scissors" and attack != "rock" and attack != "paper" :
    print("Your input is invalid")
    print("It should be: rock or paper or scissors")
else :
    print("good choice:)")
    getGameResult()


