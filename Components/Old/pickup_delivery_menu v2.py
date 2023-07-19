
# Bugs
# will only work for valid input "d" or "p"
# invalid input triggers else statement but program ask for input again

# Menu so that user can choose either pickup or delivery

print ("Do you want you order delivered or are you picking it up?")

print ("For delivery enter d")
print ("For pickup enter p")

delivery = input()

if delivery == "d":
    print ("Delivery")

elif delivery == "p":
    print ("Pickup")

else:
    print ("That was not a valid input")