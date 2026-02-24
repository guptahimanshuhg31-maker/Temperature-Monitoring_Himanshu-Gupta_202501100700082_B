import random
import time

min_temp = int(input("Enter minimum temperature: "))
max_temp = int(input("Enter maximum temperature: "))

while True:
    temp = random.randint(0, 100)
    print("Temperature:", temp)
    if temp > max_temp:
        print("Alert: Temperature is too high")
    elif temp < min_temp:
        print("Alert: Temperature is too low")
    else:
        print("Temperature is within acceptable limit")

    time.sleep(2)