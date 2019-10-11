print("What level of brightness is required?")
level_brightness_required= int(input())
#range_of_brightness= range(2, level_brightness_required,2)

print("Adjusting brightness...")

for count in range(2, level_brightness_required+1, 2):

    print("Beep's brightness level: "+ "*" * count )

    print("Bop's brightness level:  "+ "*" * count)
print("Adjustments complete!")