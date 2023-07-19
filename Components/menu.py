# list of watch models
watch_models = ['Casio Worldtime','Timex Weekender','Seiko Speedtimer','Tissot PRX 40mm','Tag Heuer Formula 1 Gulf Special Edition','Tag Heuer Monaco','Rado Captain Cook','Longines Pilot Matjek',
               'Rolex GMT Pepsi','Audemars Piguet Royal Oak','Jacob & Co Bugatti Chiron Tourbillion','Patek Phillipe Nautilus Tiffany&Co Blue']
#list of watch prices
watch_prices = [70, 85, 800, 850, 2450, 6750, 7000, 8000, 16000, 55000, 650000, 7400000]

def menu():
    number_watches = 12
    for count in range (number_watches):
        print("{} {} ${:.2f}" .format(count+1, watch_models[count], watch_prices[count]))