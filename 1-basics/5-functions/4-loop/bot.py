def cross_bridge(distance):
    print("Crossed step. " *distance ,end=" ")
    if (distance >5):
        print("The bridge is collapsing!")
    else: 
        print("We must keep going!")  



cross_bridge(3)
cross_bridge(6)