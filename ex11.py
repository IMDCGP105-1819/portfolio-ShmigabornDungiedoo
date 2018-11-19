import random
rand = random.randint(0,100)
guess=int(input("Guess the number from 0 to 100:  "))
tries=0
while guess!=rand:
    if guess>rand:
        print("Too high")
        tries=tries+1
        guess=int(input("Try again  "))
    elif guess<rand:
        print("Too low")
        tries=tries+1
        guess=int(input("Try again  "))
print("Number of tries: ", tries)
