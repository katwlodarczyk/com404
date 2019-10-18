def display_in_a_box(word):
    print("*" * (len(word) + 10))
    print("*  ", word, "    *")
    print("*" * (len(word) + 10))

def display_lower_case(word):
    print(word.lower())
     

def display_upper_case(word):
    print(word.upper())
    

def display_mirrored(word):
    reverse= ""
    for letter in word:
        reverse= letter +reverse
    print(reverse)

def repeat(word):
    print("How many times should the word be repeated?")
    how_many_times = int(input())
    for number in range (0, how_many_times, 1):
        if (number % 2 ==0):
            display_lower_case(word)
        else:
            display_upper_case(word)
    

def program():
    print("enter a word")
    word = str(input())
    print("""
    Choose one of the following options: 
    1)display in a box 
    2)display lower-case
    3)display upper-case
    4)display mirrored
    5)repeat  
    """)
    option = int(input())

    if(option == 1):
        display_in_a_box(word)
    elif(option == 2):
        display_lower_case(word)
    elif(option == 3):
        display_upper_case(word)
    elif(option == 4):
        display_mirrored(word)
    else:
        repeat(word)

program()