print("How many live cables must I avoid?")
max_live_cables = int(input())

#control var
number_of_live_cables = 0

while (number_of_live_cables < max_live_cables):
    print("Avoiding...", end="")
    number_of_live_cables = number_of_live_cables +1
    print("...Done!" + str(number_of_live_cables) + " live cable(s) avoided!")
    print("All live cables have been avoided.")