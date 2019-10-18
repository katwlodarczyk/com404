def display_ladder(steps):
    for steps in range (0, steps, 1):
        print("| |\n***")
    print("| |")


def create_ladder():
    print("How many steps?")
    steps = int(input())
    display_ladder(steps)

create_ladder()