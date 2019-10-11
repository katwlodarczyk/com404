print("How many rows should I have?")
number_of_rows = int(input())

print("How many columns should I have?")
number_of_columns = int(input())

print("Here I go:")

for rows in range(0 , number_of_rows, 1):
    for columns in range(0, number_of_columns,1):
        print(":-)" , end="")
    print()