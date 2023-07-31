#list to store ordered watches
order_list = ['Casio Worldtime','Timex Weekender','Seiko Speedtimer','Tissot PRX 40mm']
#list to store watch prices
order_cost = [70, 85, 800, 850]

customer_details = {'name':'Luka', 'phone':'0277282009', 'house':'26', 'street':'gracechurch', 'suburb':'flatbush'}

print("\n",customer_details['name'],"\n",customer_details['phone'],"\n",customer_details['house'],"\n",customer_details['street'],"\n",customer_details['suburb'])

print("\nCustomer Name: {} \nCustomer Phone: {} \nCustomer House: {} \nCustomer Street: {} \nCustomer Suburb: {}".format(  customer_details['name'],customer_details['phone'],customer_details['house'],customer_details['street'],customer_details['suburb']))


#lesson 22

count = 0
for item in order_list:
    print("Ordered: {} Cost: ${:.2f}".format(item, order_cost[count]))
    count = count+1