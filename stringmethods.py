name = input("Enter you full name:")

result= len(name) # returns length of the string including spaces
result1= name.find(" ")# returns the first occurence
result2 = name.rfind("i")# returns the last occurence

name= name.capitalize()

print(f"Hello {name}")

name= name.upper()
print(f"Hello {name}")


      

print(f"Length of the name is: {result}")
print(f"First occurence of the name is: {result1}")
print(f"Last occurence of the name is: {result2}")

result3 = name.count("i")
result4 = name.replace("i","y")

print(f"Number of 'i' in the name is: {result3}")
print(result4)

#indexing = accessing elements of a sequence using []
#           [start: end: step]

name_reversed= name[::-1]
print(f"Reversed name is: {name_reversed}")

name_list = name.split()
print(f"Name split into list: {name_list}")