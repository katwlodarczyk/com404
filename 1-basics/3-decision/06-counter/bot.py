#counter
print("Please enter the first whole number.")
first_number = int(input())
print("Please enter the second whole number.")
second_number = int(input())
print("Please enter the third whole number.")
third_number = int(input())

even_counter = 0
odd_counter= 0

if (first_number % 2 == 0):
    even_counter = even_counter+1
else:
    odd_counter = odd_counter+1

if (second_number % 2 == 0):
    even_counter =  even_counter+1
else:
    odd_counter = odd_counter+1
if (third_number % 2 ==0):
    even_counter= even_counter+1
else:
    odd_counter = odd_counter+1

print(" There are " +str(even_counter)+ " even numbers and " +str(odd_counter)+ " odd numbers")