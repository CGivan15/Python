import os
import time

shopping_list = []


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def tacos(item):
    print("\N{TACO}" * 2)

def add_to_list(item):
    show_list()
    if len(shopping_list):
        position = input("Where should I add {}?\n"
                        "Press ENTER to add to the end of the list\n"
                        "> ".format(item))
    else:
        position = 0

    try:
        position = abs(int(position))
    except ValueError:
        position = None
    if position is not None:
        shopping_list.insert(position-1, item)
    else:
        shopping_list.append(new_item)

    show_list()    

    # if item not in shopping_list:
    #     shopping_list.append(item)
    #     if len(shopping_list) < 2:
    #         print("'{}' has been added to the list.  There is currently {} item on your shopping list.".format(item, len(shopping_list)))
    #         if item.upper() == 'TACO' or item.upper() == 'TACOS':
    #             tacos(item)
    #     else:
    #         print("'{}' has been added to the list.  There are currently {} items on your shopping list.".format(item, len(shopping_list)))
    #         if item.upper() == 'TACO' or item.upper() == 'TACOS':
    #             tacos(item)
    # else:
    #     print("{} was not added since it is already on the list.".format(item))
    

def show_list():  
    clear_screen() 

    print("\nShooping List:")    
    
    for index, item in enumerate(shopping_list, start = 1):
        print("{}. {}".format(index, item))

    print("-"*10)


def remove_from_list():
    show_list()
    what_to_remove = input("What would you like to remove?\n> ")
    try:
        shopping_list.remove(what_to_remove)
    except ValueError:
        pass
        print("{} is not on your list...".format(what_to_remove))
        time.sleep(2)
    show_list()
        
def show_help():
    clear_screen()
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'LIST' to see shopping list.
Enter 'REMOVE' to delete an item from your list.
""")

show_help()
while True:
    new_item = input("> ")
    
    if new_item.upper() == "DONE" or new_item.upper() == "QUIT":
        break
    elif new_item.upper() == 'HELP':
        show_help()
        continue
    elif new_item.upper() == "LIST":
        if len(shopping_list) > 0:
            show_list()
        else:
            print("Your list is currently empty.")
        continue
    elif new_item.upper() == "REMOVE":
        remove_from_list()
    elif new_item == "":
        show_list() 
        # continue
    elif new_item[0].isspace():
        show_list()
    else:
        if new_item.upper() not in shopping_list:
            add_to_list(new_item)
        else:
            print("{} was not added since it is already on the list...".format(new_item))
            time.sleep(2)
            show_list()        

show_list()

  