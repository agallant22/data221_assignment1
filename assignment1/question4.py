# Sorted search with conditions

from random import random

values = [random() for i in range (20)]
x = random()

values.sort()
sorted_list = []

print("Value of x: ", x)

for i in values:
    if i >= x:
        sorted_list.append(i)

print("Sorted list: ", sorted_list)
print("First Matching Index: ", sorted_list[0])