for x in range(1, 11):
    print(f"{x}")

for x in reversed(range(1,11)):
    print(f"{x}")


for x in range(1, 11, 2):
    print(f"{x}")


for x in range(1,21):
    if x == 13:
        continue
    else:
        print(f"{x}")

for x in range(1,21):
    if x == 13:
        break
    else:
        print(f"{x}")

import time

my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1):
    seconds = x%60
    minutes = int(x/60)% 60
    hours = int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("TIME'S UP!!")