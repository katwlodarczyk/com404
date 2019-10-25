#initial health %
health = 100
print("Your health is 100%. Escape in progress..." + "\n")
#how many times should the program repeat
times = 5
while (times >= 1):
    print("…Oh dear, who is that?")
    response = input()
    if (response == "Smiler's Bot"):
        health = health -20 
        print("Time to jam out of here!")
    elif (response == "Hacker"):
        health = health +20
        print("Yay! Better follow this one!")
    else: 
        print("Phew, just another emoji!")
    times = times -1 
    print("\n")

print("Escaped! Health is "+ str(health) +" %.")