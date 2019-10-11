print("What strange markings do you see?")
markings= str(input())
index= 0

for position in range(0, len(markings), 1):
    print("Identifying...")
    print("Index " +str(index)+ " : " + markings[position])
    index= index+1