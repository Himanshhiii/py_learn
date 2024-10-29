#input() = A funtion that prompts the user to enter data 

name = input("What is your name?: ")
age= input("What is your age?: ")

print(f'Hello {name}')
print(f'You are now {age} years old')

#when we store user input then we store it as a string so before
#performing any operations we need to typecast it

age = int(age)
age= age+1
print(f'You will be {age} years old next year')

no_of_cakes= int(input("How many cakes would you like?: "))
print(no_of_cakes)