# list of watch models
watch_models = ['Casio Worldtime','Timex Weekender','Seiko Speedtimer','Tissot PRX 40mm','Tag Heuer Formula 1 Gulf Special Edition','Tag Heuer Monaco','Rado Captain Cook','Longines Pilot Matjek',
               'Rolex GMT Pepsi','Audemars Piguet Royal Oak','Jacob & Co Bugatti Chiron Tourbillion','Patek Phillipe Nautilus Tiffany&Co Blue']
#list of watch prices
watch_prices = [70, 85, 800, 850, 2450, 6750, 7000, 8000, 16000, 55000, 650000, 7400000]

#list to store ordered watches
order_list = []
#list to store watch prices
order_cost = []


def menu():
    number_watches = 12
    for count in range (number_watches):
        print("{} {} ${:.2f}" .format(count+1, watch_models[count],watch_prices[count]))

menu()


#ask for how mnay they would like to order
num_watches = 0


print ("")
print ("Due to scarcity, there is a limit of 12 items available for you to order. If you select more than 5 items, shipping is free. Otherwise there is a $9.00 shipping fee")




while True:
    try:
        num_watches = int(input("How many watches would you like to order? "))
        if num_watches >= 1 and num_watches <= 12: 
            break
        else: 
            print("Your order must be between 1 and 12")
    except ValueError:
        print ("That is not a valid number")
        print ("Please enter a number inbetween 1 or 12")




print(num_watches)


#choose watch from menu
#count down until all watches are ordered
print ("Please choose your watches by entering the number from the menu")
for item in range(num_watches):
    while num_watches > 0:
        watch_ordered = int(input())
        watch_ordered = watch_ordered-1
        order_list.append(watch_models[watch_ordered])
        order_list.append(watch_prices[watch_ordered])
        print("{} ${:.2f}" .format(watch_models[watch_ordered],watch_prices[watch_ordered]))
        num_watches = num_watches-1
        


#Lesson 20






