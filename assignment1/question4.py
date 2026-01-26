# Sorted search with conditions

from random import random

values = [random() for i in range (20)]
x = random()

values.sort()
sorted_list = []
print(x)

print(values)

for i in values:
    if i >= x:
        sorted_list.append(i)

print(sorted_list)