# Controlled Multiplication Loop

threshold = 100
product = 1
currentNumber = 1

while currentNumber <= threshold:
    product = product * currentNumber
    currentNumber= currentNumber + 1
print(currentNumber)

print("final product: ", product)
print("final current number: " + str(currentNumber))