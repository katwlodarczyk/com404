#review, if elif else, nested dicisions, or operator, and operator
print("what is the weather outside?")
weather = input()


if (weather == "sunny"):
    print("whats my mood today?")
    mood = input()
    if ((weather == "sunny") and (mood == "happy")):
        print("I will go to the park and play!")
    else:
        print("I will go to the garden and sunbathe alone")
elif ((weather == "rainy") or (weather == "foggy")):
    print("I will stay inside and read a book!")
elif (weather == "cold"):
    print("do I want to go outside? yes/no")
    go_outside = input()
    if (go_outside == "yes"):
        print("I will dress warmly and go out!")
    else:
        print("I'd rather stay inside...")
else:
    print("I still need to think what to do today...")