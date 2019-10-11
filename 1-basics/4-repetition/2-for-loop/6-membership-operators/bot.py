print("What phrase do you see?")
phrase= input()
reverse= ""

for letter in phrase:
    reverse= letter+ reverse

print(reverse)