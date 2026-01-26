# Nested Dictionary from String

words = ["data", "science"]

def dictionary_from_list(words):
    result = {}
    for i in words:
        length = len(i)
        if len(i) % 2 == 0:
            parity = "even"
        else:
            parity = "odd"
        result[i] = {
            "length": length,
            "parity": parity
        }
    print(result)

dictionary_from_list(words)