print("How many numbers should I sum up?")
how_many_numbers= int(input())

#control var
asked_number_times= 0
total = 0

while(asked_number_times < how_many_numbers):
    asked_number_times= asked_number_times+1
    print("Please enter number " +str(asked_number_times)+ " of " +str(how_many_numbers) )
    number= int(input())
    total= total+number

print("The answer is "+ str(total))