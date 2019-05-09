def combo(iterable1, iterable2):
    output = []
    for i in range(0, len(iterable1)):
        output += (iterable1[i], iterable2[i]),
    return output

print(combo("sipr", "lpey"))