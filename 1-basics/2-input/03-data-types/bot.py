print("What is you name human?")
name = input()
print(name)
print("How old are you (in years)?")
age = int(input())
print("How tall are you (in meters)?")
height = float(input())
print("How much do you weigh (in kilograms)?")
weight = int(input())

bmi = weight / (height*height)

print(name+ "you are " +str(age)+ " years old and your BMI is " +str(bmi))