dead_ends= 0
number_of_mummies = 0

print("Escaping the tomb...")

times = 0
while (times <4):
    print("\n")
    print("What lies before me?")
    response = input()
    if (response == "dead end"):
        dead_ends = dead_ends +1
        print("Time to turn back")
    elif(response == "a mummy"):
        number_of_mummies = number_of_mummies +1
        print("Better find another way")
    else:
        print("Let's move around it.")
    times= times+1

print("Encountered "+ str(dead_ends) + " dead ends and " +str(number_of_mummies) + " mummies.")