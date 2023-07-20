# list of watch models
watch_models = ['Casio Worldtime','Timex Weekender','Seiko Speedtimer','Tissot PRX 40mm','Tag Heuer Formula 1 Gulf Special Edition','Tag Heuer Monaco','Rado Captain Cook','Longines Pilot Matjek',
               'Rolex GMT Pepsi','Audemars Piguet Royal Oak','Jacob & Co Bugatti Chiron Tourbillion','Patek Phillipe Nautilus Tiffany&Co Blue']
#list of watch prices
watch_prices = [70, 85, 800, 850, 2450, 6750, 7000, 8000, 16000, 55000, 650000, 7400000]


def menu():
    number_watches = 12
    for count in range (number_watches):
        print("{} {} ${:.2f}" .format(count+1, watch_models[count], watch_prices[count]))


#ask for how mnay they would like to order
num_watches = 0

print ("")
print ("Due to scarcity, there is a limit of 12 items available for you to order. If you select more than 5 items, shipping is free. Otherwise there is a $9.00 shipping fee")

num_watches = input("How many watches would you like to order? ")

print(num_watches)


#choose watch from menu
print ("Please choose your watches by entering the number from the menu")
for item in range(num_watches):







#count down until all watches are ordered


