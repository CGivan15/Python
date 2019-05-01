sodas = ["Pepsi", "Cherry Coke Zero", "Sprite"]
chips = ["Doritos", "Fritos"]
candy = ["Snickers", "M&Ms", "Twizzlers"]

while True:
    choice = input("""
    What would you like from the Vending Machine?
    Options:
        SODA        
        CHIPS
        CANDY
        NOTHING 
    > """).lower()

    try:
        if choice == 'soda':
            snack = sodas.pop()
        elif choice == 'chips':
            snack = chips.pop()
        elif choice == 'candy':
            snack = candy.pop()
        elif choice == 'nothing':
            break
        else:
            print("Sorry, I didn't understand that.")
            continue
    except IndexError:
        print("We're all out of {}! Sorry!".format(choice))
    else:
        print("Here's your {}: {}".format(choice, snack))
    
    if len(sodas + chips + candy) == 0:
        print("The Vending Machine is Empty.  Please come back later.")
        break
