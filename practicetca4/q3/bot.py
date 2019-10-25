print("How many heroes must we gather?")
how_many= int(input())
print("Gathering heroes…")
for number in range (1, how_many+1 ,1):
    print("…found hero "+ str(number))
print("...all the heroes have been gathered.")   