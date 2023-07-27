#list to store ordered watches
order_list = ['Casio Worldtime','Timex Weekender','Seiko Speedtimer','Tissot PRX 40mm']
#list to store watch prices
order_cost = [70, 85, 800, 850]



count = 0
for item in order_list:
    print("Ordered: {} Cost: ${:.2f}".format(item, order_cost[count]))
    count = count+1