print("Welcome to the Planet of the Apes…")

times = 0
human_encountered = 0
ape_encountered = 0

for number in range(0,7,1):
    print("…be ye human or be ye ape?")
    response = input()
    if (response == "human"):
        human_encountered = human_encountered+1
        print("I did not start this war. But I will finish it.")
    elif (response == "ape"):
        ape_encountered = ape_encountered+1
        print("Apes together strong!")
    else:
        print("This is not your fight.")
    
print("Total human encountered: "+ str(human_encountered))
print("Total apes encountered: "+ str(ape_encountered))