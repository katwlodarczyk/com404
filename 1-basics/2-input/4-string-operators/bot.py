print("Please enter the number of lives")
no_of_lives = int(input())
print("Please enter the energy level")
energy_level = int(input())
print("Please enter the shield level")
sheild_level = int(input())

print("""Health has been set

Lives: """ +str(no_of_lives * '♥')+ """
Energy: """ +str(energy_level *'♦')+ """
Shield: """ +str(sheild_level *'♦')
)
