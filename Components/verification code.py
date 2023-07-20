# validates inputs to check if they are blank
def not_blank(question): 
    valid = False
    while not valid:
        response = input(question)
        if response != "":
            return response.title()
        else:
            print("This can not be blank")