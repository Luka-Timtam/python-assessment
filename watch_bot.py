# Watch Bot Program


import random
from random import randint

# List of random names
names = ["Luka", "kade", "Jayden", "Jason", "Max verstappen", "Michael Schumacher", "Rory", "Antonie", "Lucas", "Charles Leclerc"]
# list of watch models
watch_models = ['Casio Worldtime','Timex Weekender','Seiko Speedtimer','Tissot PRX 40mm','Tag Heuer Formula 1 Gulf Special Edition','Tag Heuer Monaco','Rado Captain Cook','Longines Pilot Matjek',
               'Rolex GMT Pepsi','Audemars Piguet Royal Oak','Jacob & Co Bugatti Chiron Tourbillion','Patek Phillipe Nautilus Tiffany&Co Blue']
#list of watch prices
watch_prices = [70, 85, 800, 850, 2450, 6750, 7000, 8000, 16000, 55000, 650000, 7400000]
# Customer details dictonary
customer_details = {}

# validates inputs to check if they are blank
def not_blank(question): 
    valid = False
    while not valid:
        response = input(question)
        if response != "":
            return response.title()
        else:
            print("This can not be blank")

# Welcome message with random name
def welcome():
    '''
    Purpose: To generate a random name from the list and print out 
    a welcome message
    Parameters: None
    Returns: None
    '''
    num = randint(0,9)
    name = (names[num])
    print("*** Welcome to Timmermans Watches ***")
    print("*** My name is",name, "***")
    print("*** I will be here to help you find your next timepiece ***")

# Menu for pickup or delivery

def order_type():
    print ("Is your order for pickup or delivery?")
    print ("For pickup please enter 1")
    print ("For delivery please enter 2")
    while True:
        try: 
            delivery = int(input("Please enter a number: "))
            if delivery >= 1 and delivery <= 2:
                if delivery == 1:
                    print ("Pickup")
                    pickup_info()
                    break
                elif delivery == 2:
                    print ("Delivery")
                    delivery_info()
                    break
            else:
                print ("The number must be 1 or 2")
        except ValueError:
            print ("That is not a valid number")
            print ("Please enter 1 or 2")




# Pick up information
def pickup_info():
    question = ("Please enter your name: ")
    customer_details['name'] = not_blank(question)
    print (customer_details['name'])

    question = ("Please enter your phone number: ")
    customer_details['phone'] = not_blank(question)
    print (customer_details['phone'])
    print(customer_details)





# Delivery information - name address and phone
def delivery_info():
    question = ("Please enter your name: ")
    customer_details['name'] = not_blank(question)
    print (customer_details['name'])

    question = ("Please enter your phone number: ")
    customer_details['phone'] = not_blank(question)
    print (customer_details['phone'])

    question = ("Please enter your house number: ")
    customer_details['house'] = not_blank(question)
    print (customer_details['house'])

    question = ("Please enter your street: ")
    customer_details['street'] = not_blank(question)
    print (customer_details['street'])

    question = ("Please enter your suburb: ")
    customer_details['suburb'] = not_blank(question)
    print (customer_details['suburb'])


# Watch menu 
def menu():
    number_watches = 12
    for count in range (number_watches):
        print("{} {} ${:.2f}" .format(count+1, watch_models[count], watch_prices[count]))




# Choose total number of watches
def order_watches():
    print("")
    print("Due to scarcity, there is a limit of 12 items available for you to order. If you select more than 5 items, shipping is free. Otherwise there is a $9.00 shipping fee")
    print ("How many watches would you like to order?")
    while True:
                num_watches = int(input("Please enter a number: "))
                if num_watches >= 1 and num_watches <= 12:
                    print("You have chosen to order",num_watches, "watches")
                    break
                else:
                    print ("The number must be between 1 and 12")






# Watch order - from menu - print each watch ordered with cost





# Print order out - including if order is delivery or pickup and names and price of each watch  - total cost including any delivery charge




# Ability to cancel or proceed with order





# Option for new order or to exit







# Main function

def main():
    '''
    Purpose: To run all functions 
    a welcome message
    Parameters: None
    Returns: None
    '''
    welcome()
    order_type()
    menu()
    order_watches()

main()

