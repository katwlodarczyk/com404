def under(word):
    print(word)
    print("*" * len(word))

def over(word):
    print("*" * len(word))
    print(word)

def both(word):
    print("*" * len(word))
    print(word)
    print("*" * len(word))

def grid(word):
    print("What's the size of the grid?")
    size_of_grid = int(input())

    for row in range(0, size_of_grid, 1):
        print( (("*" * len(word)) + "     ") * size_of_grid)

        for col in range(0,size_of_grid,1):
            if (col == size_of_grid - 1):
                print(word, end="")
            else:
                print( (word + "  |  "), end="")
        print()

    print( (("*" * len(word)) + "     ") * size_of_grid)



def program():
    print("Enter the word")
    word= input()
    print("""
    Choose one of the options shown below:
    1) Under - display the word with a line under it.
    2) Over - display the word with a line over it.
    3) Both - display the word in an underline and overline.
    4) Grid - display the word in a grid that is n x n in size.
    """)
    option= int(input())
    if (option == 1):
        under(word)
    elif( option ==2):
        over(word)
    elif(option == 3):
        both(word)
    else:
        grid(word)

program()
