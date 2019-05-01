def favorite_food(dict):    
    return "Hi, I'm {name} and I love to eat {food}!".format(**dict)

likes = {"name": "Victoria", "food": "tacos"}

print(favorite_food(likes))


# E.g. word_count("I do not like it Sam I Am") gets back a dictionary like:
# {'i': 2, 'do': 1, 'it': 1, 'sam': 1, 'like': 1, 'not': 1, 'am': 1}
# Lowercase the string to make it easier.

def word_count(string):
    words = string.lower().split()
    dictionary = {}
    for word in words:
        dictionary[word] = 0
    for word in words:
        dictionary[word] += 1
    print(dictionary)
    return dictionary

word_count("I do not like it Sam I Am")
word_count("How much wood could a woodchuck chuck if a woodchuck could chuck wood")

