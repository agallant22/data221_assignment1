# Safe Function Application

def exponent(x, y):
    return x ** y

pairs = [[5, 2], [3, -1], [4, 3], [2,0]]
results = []

for x, y in pairs:
    if y < 0:
        continue
    results.append(exponent(x, y))

print(results)