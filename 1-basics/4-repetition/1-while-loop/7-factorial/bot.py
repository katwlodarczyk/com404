print("Please enter a number:")
entered_number= int(input())

sum_of_multiplication= 0

#control var
number_count= 1


while( number_count <= entered_number):
    sum_of_multiplication= sum_of_multiplication * number_count
    number_count= number_count+1
    

print("The factorial is "+ str(sum_of_multiplication))