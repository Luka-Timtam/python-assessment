def order_type(low, high, question):
    while True:
        try: 
            num = int(input(question))
            if num >= low and num <= high:
                return num
            else:
                print (f"enter a number between {low} and {high}")
        except ValueError:
            print ("That is not a valid number")
            print (f"enter a number between {low} and {high}")


LOW = 1
HIGH = 2

question = (f"enter a number between {LOW} and {HIGH}")

answer = order_type(LOW, HIGH, question)

print(answer)