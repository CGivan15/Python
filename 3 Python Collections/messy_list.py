messy_list = ["a", 2, 3, 1, False, [1, 2, 3]]

print("This is your messy list: {}".format(messy_list))

# Your code goes below here
messy_list.insert(0, messy_list.pop(3))
messy_list.remove("a") 
messy_list.remove(False)
messy_list.remove([1, 2, 3])

print("Here is your cleaned up list containing only integers: {}".format(messy_list))