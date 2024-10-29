#list, set and tuple

#LIST
fruits = ["apple", "orange", "banana", "coconut"]

print(fruits[0: 3])
print(fruits[: 3])
print(fruits[::2])

fruits.append("pineapple")
fruits.remove("orange")
fruits.sort()
fruits.reverse()
index =fruits.index("pineapple")
#fruits.clear()

print(fruits, index)
print("orange" in fruits)

#SET

fruits = {"apple", "orange", "banana", "coconut"}

#print(dir(fruits))
#print(help(fruits))

fruits.add("pineapple")
fruits.remove("orange")
fruits.pop()
print(fruits)

#TUPLE

fruits = ("apple", "orange", "banana", "coconut")
print(fruits.index("apple"))
print(fruits.count("pineapple"))


