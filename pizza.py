bill = 0


access_pizza = str(input("do you want to buy pizza? Y or N ")).lower()
if access_pizza.lower() == "y":
    print("you have access to order pizza")
    size = str(input("Enter your size of pizza "))
    if size == "L":
        bill = 25
    elif size == "M":
        bill = 20 
    elif size == "S":
        bill = 15 
    else:
        print("Invalid Entry")
        exit ()
    # print(f"Your bill is: {bill} ")

    add_pep = input("Do you want pepperoni? Y or N")
    if add_pep == "Y":
        if size == "L":
            bill = bill + 3
        elif size == "M":
            bill = bill + 3
        else:
            bill += 2
    
    # print(f"Your bill is: {bill} ")

    add_cheese = input("Do you want cheese? Y or N")
    if add_cheese == "Y":
        bill = bill + 1
    print(f"Your bill is: {bill} ")
else:
    print("you have no access")
    exit ()
    
 




