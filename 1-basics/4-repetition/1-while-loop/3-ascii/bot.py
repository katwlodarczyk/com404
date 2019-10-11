print("How many bars should be charged?")
max_bars = int(input())

#control var
number_charged = 0

while (number_charged < max_bars):
    print("Charging:", end=" ")
    number_charged= number_charged+1
    print(str(number_charged)+ " out of " +str(max_bars)+ " charged.")

    
print("The battery is fully charged.")
    