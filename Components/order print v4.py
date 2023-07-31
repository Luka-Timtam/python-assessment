#list to store ordered watches
order_list = ['Casio Worldtime','Timex Weekender','Seiko Speedtimer','Tissot PRX 40mm']
#list to store watch prices
order_cost = [70, 85, 800, 850]

customer_details = {'name':'Luka', 'phone':'0277282009', 'house':'26', 'street':'gracechurch', 'suburb':'flatbush'}

def print_order():
    total_cost = sum(order_cost) 
    print("Customer Details")
    print(f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']} \nCustomer Address: {customer_details['house']} {customer_details['street']} {customer_details['suburb']}")
    print()
    print("Order Details")
    count = 0
    for item in order_list:
        print("Ordered: {} Cost: ${:.2f}".format(item, order_cost[count]))
        count = count+1
    print()
    print("Order Cost Details")
    print(f"Total: ${total_cost}")
print_order()
