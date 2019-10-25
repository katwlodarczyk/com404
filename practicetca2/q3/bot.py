print("How many miles must I travel before I reach the secret base?")
response = int(input())
print("I will count the miles...")
for number in range ( response, 0, -1):
    print("I have "+ str(number) + " miles to go before I reach the base.")
print("I have arrived at the secret headquarters of the MIB!")
print("It is time to sneak in.")