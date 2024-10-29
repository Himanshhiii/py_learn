#OR AND NOT

temp = 25
is_raining = False


if temp > 35 or temp < 0 or is_raining == False:
    print("It's too hot or cold or it's not raining.")
else:
    print("It's a good day to go outside.")

if is_raining == True and temp < 20 :
    print("It's a bit cold but we can still go outside.")
else:
    print("It's not too cold or it's raining.")


# conditional expressions X if condition else Y

num = 5

print("Postive" if num >0 else "Negative")

num = 6
result= "EVEN " if num % 2 ==0 else "ODD"
print(result)

#max_num =  a if a>b else b
#min_num = a if a<b else b