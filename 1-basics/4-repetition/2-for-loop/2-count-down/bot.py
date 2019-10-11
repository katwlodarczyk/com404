print("How far are we from the cave?")
distance= int(input()) 


for count in range (distance,0, -1):
    print( str(count) + " step(s) remaining.")


print("We have reached the cave!")