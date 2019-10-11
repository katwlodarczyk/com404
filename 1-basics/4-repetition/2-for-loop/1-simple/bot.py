print("How many mountains should I display?")
mountains_to_display= int(input())

print("Displaying...")
for count in range(0, mountains_to_display, 1):
    print("""   
           __
          /  \_  
         /^    \\
        /  ^    \_
      _/ ^ ^  ^   \\
     /  ^     ^    \\
""")

print("Done!")
