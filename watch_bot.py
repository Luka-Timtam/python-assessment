# Watch Bot Program

import sys
import random
from random import randint

# List of random names
names = ["Luka", "kade", "Jayden", "Jason", "Max verstappen",
         "Michael Schumacher", "Rory", "Antonie", "Lucas", "Charles Leclerc"]
# list of watch models
watch_models = ['Casio Worldtime', 'Timex Weekender', 'Seiko Speedtimer', 'Tissot PRX 40mm', 'Tag Heuer Formula 1 Gulf Special Edition', 'Tag Heuer Monaco', 'Rado Captain Cook', 'Longines Pilot Matjek',
                'Rolex GMT Pepsi', 'Audemars Piguet Royal Oak', 'Jacob & Co Bugatti Chiron Tourbillion', 'Patek Phillipe Nautilus Tiffany&Co Blue']
# list of watch prices
watch_prices = [70, 85, 800, 850, 2450, 6750,
                7000, 8000, 16000, 55000, 650000, 7400000]
# Customer details dictonary
customer_details = {}
# list to store ordered watches
order_list = []
# list to store watch prices
order_cost = []

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
    num = randint(0, 9)
    name = (names[num])
    print("*** Welcome to Timmermans Watches ***")
    print("*** My name is", name, "***")
    print("*** I will be here to help you find your next timepiece ***")


# validates inputs for if they are blank or integer
def order_type():
    del_pick = ""
    print("Is your order for pickup or delivery?")
    print("For pickup please enter 1")
    print("For delivery please enter 2")
    while True:
        try:
            delivery = int(input("Please enter a number: "))
            if delivery >= 1 and delivery <= 2:
                if delivery == 1:
                    print("Pickup")
                    pickup_info()
                    del_pick = "pickup"
                    break
                elif delivery == 2:
                    print("Delivery")
                    delivery_info()
                    del_pick = "delivery"
                    break
            else:
                print("The number must be 1 or 2")
        except ValueError:
            print("That is not a valid number")
            print("Please enter 1 or 2")
    return del_pick


# Pick up information
def pickup_info():
    question = ("Please enter your name: ")
    customer_details['name'] = not_blank(question)
    print(customer_details['name'])

    question = ("Please enter your phone number: ")
    customer_details['phone'] = not_blank(question)
    print(customer_details['phone'])


# Delivery information - name address and phone
def delivery_info():
    question = ("Please enter your name: ")
    customer_details['name'] = not_blank(question)
    print(customer_details['name'])

    question = ("Please enter your phone number: ")
    customer_details['phone'] = not_blank(question)
    print(customer_details['phone'])

    question = ("Please enter your house number: ")
    customer_details['house'] = not_blank(question)
    print(customer_details['house'])

    question = ("Please enter your street: ")
    customer_details['street'] = not_blank(question)
    print(customer_details['street'])

    question = ("Please enter your suburb: ")
    customer_details['suburb'] = not_blank(question)
    print(customer_details['suburb'])


# Watch menu
def menu():
    number_watches = 12
    for count in range(number_watches):
        print("{} {} ${:.2f}" .format(
            count+1, watch_models[count], watch_prices[count]))


# Choose total number of watches
def order_watches():
    # ask for how mnay they would like to order
    num_watches = 0
    print("")
    print("Due to scarcity, there is a limit of 12 items available for you to order. If you select more than 5 items, shipping is free. Otherwise there is a $9.00 shipping fee")
    while True:
        try:
            num_watches = int(
                input("How many watches would you like to order? "))
            if num_watches >= 1 and num_watches <= 12:
                break
            else:
                print("Your order must be between 1 and 12")
        except ValueError:
            print("That is not a valid number")
            print("Please enter a number inbetween 1 or 12")
    # choose watch from menu
    # count down until all watches are ordered
    for item in range(num_watches):
        while num_watches > 0:
            while True:
                try:
                    watch_ordered = int(
                        input("Please choose your watches by entering the number from the menu "))
                    if watch_ordered >= 1 and watch_ordered <= 12:
                        break
                    else:
                        print("Your order must be between 1 and 12")
                except ValueError:
                    print("That is not a valid number")
                    print("Please enter a number inbetween 1 or 12")
            watch_ordered = watch_ordered-1
            order_list.append(watch_models[watch_ordered])
            order_cost.append(watch_prices[watch_ordered])
            print("{} ${:.2f}" .format(
                watch_models[watch_ordered], watch_prices[watch_ordered]))
            num_watches = num_watches-1


# Watch order - from menu - print each watch ordered with cost
# Print order out - including if order is delivery or pickup and names and price of each watch  - total cost including any delivery charge
def print_order(del_pick):
    print()
    total_cost = sum(order_cost)
    print("Customer Details")
    if del_pick == "delivery":
        print("Your order is for Delivery")
        if len(order_list) < 6:
            total_cost = total_cost + 12
            print("You have ordered 5 or less items, a $12 delivery charge will incur")
        print(
            f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']} \nCustomer Address: {customer_details['house']} {customer_details['street']} {customer_details['suburb']}")
    elif del_pick == "pickup":
        print("Your order is for Pickup")
        print(
            f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']}")

    print()
    print("Order Details")
    count = 0
    for item in order_list:
        print("Ordered: {} Cost: ${:.2f}".format(item, order_cost[count]))
        count = count+1
    print()
    print("Order Cost Details")
    print(f"Total: ${total_cost}")


# Ability to cancel or proceed with order
def confirm_cancel():
    print("Please confirm your order below: ")
    print("To confirm please enter 1")
    print("To cancel please enter 2")
    while True:
        try:
            confirm = int(input("Please enter a number: "))
            if confirm >= 1 and confirm <= 2:
                if confirm == 1:
                    print("Order Confirmed")
                    print("Your order is being processed and will be sent to you soon")
                    print("You will receive a TXT message soon with a tracking code")
                    new_exit()
                    break

                elif confirm == 2:
                    print("Your order has been cancelled")
                    print("You can restart your order or exit the BOT")
                    new_exit()
                    break
            else:
                print("The number must be 1 or 2")
        except ValueError:
            print("That is not a valid number")
            print("Please enter 1 or 2")


# Option for new order or to exit
def new_exit():
    print("Do you want to start another order or exit?: ")
    print("To start another order please enter 1")
    print("To exit the BOT please enter 2")
    while True:
        try:
            confirm = int(input("Please enter a number: "))
            if confirm >= 1 and confirm <= 2:
                if confirm == 1:
                    print("New Order")
                    order_list.clear()
                    order_cost.clear()
                    customer_details.clear()
                    main()
                    break

                elif confirm == 2:
                    print("Exit")
                    order_list.clear()
                    order_cost.clear()
                    customer_details.clear()
                    sys.exit()
                    break
            else:
                print("The number must be 1 or 2")
        except ValueError:
            print("That is not a valid number")
            print("Please enter 1 or 2")


# Main function

def main():
    '''
    Purpose: To run all functions 
    a welcome message
    Parameters: None
    Returns: None
    '''
    welcome()
    del_pick = order_type()
    menu()
    order_watches()
    print_order(del_pick)
    confirm_cancel()


main()
