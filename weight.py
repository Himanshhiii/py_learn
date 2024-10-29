#python weight converter

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds?(Kgs or Lbs): ")

if unit =='Kgs':
    weight *= 2.205
    unit ="Lbs"
elif unit == 'L':
    weight /= 2.205
    unit ="Kgs"
else:
    print("Invalid unit. Please enter either 'Kgs' or 'Lbs'.")

print(f"Your converted weight is: {round(weight,1)}{unit}")