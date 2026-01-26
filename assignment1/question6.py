# Distribution Analysis

def distributionAnalysis(numbers):
    total = len(numbers)
    result = {}

    for i in set(numbers):
        count = 0
        for j in numbers:
            if i >= j:
                count += 1
            result[i] = (count / total) * 100

    return result

numbers = [3, 1, 2, 3, 4, 2]

print(distributionAnalysis(numbers))