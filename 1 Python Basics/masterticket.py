SERVICE_CHARGE = 2
TICKET_PRICE = 10

tickets_remaining = 100

def calculate_price(num_tickets):
    return (num_tickets * TICKET_PRICE) + SERVICE_CHARGE

while tickets_remaining >= 1:
    print("\nThere are {} tickets remaining.".format(tickets_remaining))    
    name = input("What is your name? ")    
    try:
        number_of_tickets = int(input("Hello, {}. How many tickets would you like? ".format(name)))
        if number_of_tickets > tickets_remaining:
            raise ValueError("Can you read, {}.  There are only {} tickets remaining.  Try again, genius...".format(name, tickets_remaining))
        elif number_of_tickets < 1:
            raise ValueError("\n...\nSeriously?!? You're trying to order {} tickets???\nDoes that seem logical??? You can't request less than 1 ticket, dummy!".format(number_of_tickets))
    except ValueError as err:
        print("There is an error. {}. Enter a valid number, moron.".format(err))
    except TypeError:
        print("{}, What the F*@& are you doing?  Pay attention, nitwit!".format(name))
    else:
        amount_due = calculate_price(number_of_tickets)
        print("For {} tickets, the total due is ${}.".format(number_of_tickets, amount_due))
        confirm = input("Do you want to proceed? Y/N  ").upper()
        if confirm == "Y":
            # TODO: Gather credit card information and process it.
            
            print("SOLD!\nThanks for your purchase, {}.  Enjoy the show!".format(name))
            tickets_remaining -= number_of_tickets
        elif confirm == "N":
            print("Thanks, {}.  Next time don't waste my time.".format(name))
        else:
            print("Enter a valid selection, idiot!  I said Y or N... Sheesh!")

print("\nThis event is sold out.\nNow get off my lawn, hippies.\n")                