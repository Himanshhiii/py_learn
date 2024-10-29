fruits= ["apple", "orange", "coconut", "banana"]
vegetables= ["celery", "carrots", "potatotes", "peas"]
meats= ["chicken", "fish", "turkey"]

groceries =[fruits, vegetables, meats]

print(groceries[2])
print(groceries[0][2])

#groceries = [["apple", "orange", "coconut", "banana"],
#             ["celery", "carrots", "potatotes", "peas"],
#             ["chicken", "fish", "turkey]]


#we can use nested loops to iterate over the 2D list

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()

# 2D tuple

num_pad = ((1, 2, 3), 
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:
    for x in row : 
        print(x, end=" ")
    print()
