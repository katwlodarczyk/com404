
def under(message):
    print("Halloween")
    print("-" * len(message))
    print(message)

def over(message):
    print(message)
    print("-" * len(message))
    print("Halloween.")

def both(message):
    print(message)
    print("-" * len(message))
    print("Halloween")
    print("-" * len(message))
    print(message)

def grid(message):
    print("Halloween | " * len(message))

def program():
    print("Enter a message")
    message= input()
    print("""
    Choose one of the options:
    1) Under - display the word "Halloween" with a line under it and then the message under the line.  The length of the line should be the same as the message entered by the user. 
    2) Over - display the message with a line under it followed by the word "Halloween". The length of the line should be the same as the message entered by the user. 
    3) Both - display the message above and below the word "Halloween".
    4) Grid - display the word "Halloween" in a grid that is n x n in size where the size of the grid is determined by the length of the message (with maximum of 5).
    """
    )
    option= int(input())

    if (option == 1):
        under(message)
    elif (option == 2):
        over(message)
    elif (option == 3):
        both(message)
    elif (option == 4):
        grid(message)
    else:
        print("There is no option " + option)

program()