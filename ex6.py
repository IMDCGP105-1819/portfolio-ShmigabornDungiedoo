name=input("What is your name?")
age=int(input("How old are you?"))
height=int(input("What is your height in cm?"))
weight=int(input("What is your weight in kg?"))
eye_colour=input("What is your eye colour?")
hair_colour=input("What is yoour hair colour?")

if age>=18:
    print(name + " is an adult")
else:
    print(name + " can't buy beer yet")

if weight > 200:
    print("Maybe you should go to gym")
else:
    print("Your weight is ok")

if height >= 200:
    print("You could be a basketball player")
else:
    print("More or less average height")
