def is_slow_zombie(speed):
    if (speed < 5):
        return True
    else:
        return False
    
def take_action(mutation, speed):
    is_slow_zombie(speed)
    if (is_slow_zombie(speed) == True):
        print("This "+ mutation + " zombie is a slow zombie. You can run around it!")
    else:
        print("This "+ mutation + " zombie is a fast zombie. You better hide!")
    
def run():
    print("Enter the mutation type")
    mutation = input()
    print("Enter the speed of the zombie")
    speed = int(input())
    print("Should I identify or action?")
    answer= input()

    if (answer == "identify"):
        is_slow_zombie(speed)
    elif(answer == "action"):
        take_action(mutation,speed)
    else: 
        print("Unkown zombie!")

run()