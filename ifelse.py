age= int(input("Enter age: "))

if(age>18):
    print("You are eligible to vote")
elif age<0:
    print("Invalid age")
elif age>100:
    print("Age cannot be greater than 100")
else:
    print("You are not eligible to vote")