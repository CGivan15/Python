def disemvowel(word):
    result = ""
    for letter in word:
        if letter.upper() not in 'AEIOU':
            result += letter
        else:
            pass
    print("Your disemvowelled word is: {}".format(result)) 
    return result

word = input("Enter a word to disemvowel: ")
disemvowel(word)

   