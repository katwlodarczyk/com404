print("How many zones must I cross?")
how_many = int(input())
print("Crossing zones...")
for number in range ( how_many, 0, -1):
    print("…crossed zone " + str(number))
print("Crossed all zones. Jumanji!")