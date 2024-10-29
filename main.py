#This is my first python program
print("I am Himanshi Sharma")
print("I am a student")

#variables: string, integer, float, boolean

#String

first_name= "Himanshi"
print(first_name)
print(f"Hello {first_name}")

# f means format, that is the easiet way to print variables

#Integer

age= 47
print(f"I am {age} years old")

#Float

price= 10.99
print(f"The price is ${price}")

gpa= 3.7
print(f"my current gpa is {gpa}")

#Boolean

is_student= True
#is_student=False

if is_student:
    print("I am a student")
else:
    print("I am not a student")

#Typecasting: converting a variable from one data type to another

name="Himanshi"
age=21
gpa=8.1
is_student= True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

gpa= int(gpa)
print(type(gpa))
print(gpa)

age= float(age)
print(type(age))
print(age)

name= bool(name)
print(name)

name= int(name) #invalid literal for int() with base 10: 'Himanshi'
print(name)

name=float(name)
print(name)