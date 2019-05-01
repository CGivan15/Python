shopping_list = []

def tacos(item):
    print("\N{TACO}" * 2)

def add_to_list(item):
    if item not in shopping_list:
        shopping_list.append(item)
        if len(shopping_list) < 2:
            print("'{}' has been added to the list.  There is currently {} item on your shopping list.".format(item, len(shopping_list)))
            if item.upper() == 'TACO' or item.upper() == 'TACOS':
                tacos(item)
        else:
            print("'{}' has been added to the list.  There are currently {} items on your shopping list.".format(item, len(shopping_list)))
            if item.upper() == 'TACO' or item.upper() == 'TACOS':
                tacos(item)
    else:
        print("{} was not added since it is already on the list.".format(item))


def show_list():    
    print("\nShooping List:")    
    for item in shopping_list:
        print("* " + item)
        
        
def show_help():
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'LIST' to see shopping list.
""")

show_help()
while True:
    new_item = input("> ")
    
    if new_item == "DONE":
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == "LIST":
        if len(shopping_list) > 0:
            show_list()
        else:
            print("Your list is currently empty.")
        continue        
    add_to_list(new_item)

show_list()

  