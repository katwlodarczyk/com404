def is_league_united(hero1, hero2):
    if (hero1 == "Superman" and hero2 == "Wonder Woman"):
        return True
    else:
        return False

def decide_plan(hero1, hero2):
    is_league_united(hero1,hero2)
    if (is_league_united(hero1, hero2) == True):
        return "Time to save the world!"
    else:
        return "We must unite the league!"

def run():
    print("What is the name of the first hero?")
    hero1= input()

    print("What is the name of the second hero?")
    hero2= input()

    print("league or plan?")
    response= input()

    if(response == "league"):
        print(is_league_united(hero1,hero2))
    elif(response == "plan"):
        print(decide_plan(hero1,hero2))
    else:
        print("Invalid command. Please try again.")

#run the program
run()
