def stringcases (string):
    uppercase = string.upper()
    lowercase = string.lower()
    titlecase = string.title()
    reverse = string[::-1]
    return print("Uppercase: {}, Lowercase: {}, Titlecase: {}, Reverse: {}.".format(uppercase, lowercase, titlecase, reverse))


def stringcases2(my_string):
      uppercase = tuple(list(my_string.upper()))
      lowercase = tuple(list(my_string.lower()))
      titlecase = tuple(list(my_string.title()))
      reverse = tuple(list(my_string[::-1]))
      return print(uppercase, lowercase, titlecase, reverse)    

stringcases("pErrY")    
stringcases2("liVEs")    