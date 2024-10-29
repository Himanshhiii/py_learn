name = input("Enter your name:")

while name== "":
    print("Name cannot be empty. Please enter your name again:")
    name = input("Enter your name:")

print(f"Hello {name}")


food = input("Enter the food that you wish to eat (q to quit): ")

while not food == "q":
    print(f"You wish to eat {food}")
    food = input("Enter another food that you wish to eat (q to quit): ")

print("Thank you for your input. Goodbye!")

num= int(input("Enter the number between 1 - 10: "))

while num<1 or num>10:
    print("Invalid input. Please enter a number between 1 and 10:")
    num = int(input("Enter the number between 1 - 10: "))

print(f"The number you entered is {num}")