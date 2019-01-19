####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "January_Bakery" #complete me!
signature_flavors = ["cereal","birthday_cake","dates"]#complete me!
order_list = []


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    # your code goes here!
print(menu) #for key,value in menu.items():
            #print(key,value)

def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    # your code goes here!
    for cupcake in original_flavors:
        print(cupcake)


def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    # your code goes here!
    for signatures in signature_flavors:
        print(signatures)

def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    # your code goes here!
    if order in signature_flavors:
        return  True
    elif order in original_flavors:
        return True 
    elif order in menu:
        return True
    else:
        return False  

def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    user_input = input("What's your order?\n or type exit to checkout\n")# your code goes here!
    while user_input.lower() != "exit":
        if is_valid_order(user_input.lower()) == True:
            order_list.append(user_input)
            print("[%s] has been added to the cart" % user_input)
            user_input=input("What else?")
        else:
            print("You blind? not in the menu")
            user_input=input("please enter a valid input")
    return order_list


def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    # your code goes here!
    if total >= 5:
        print("We can use the credit card")
    else: 
        print("Cash Only")

def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    # your code goes here!
    for order in order_list:
        if order in original_flavors:
            total += 2 
        elif order in signature_flavors:
            total += 2.75
        else:
            total += menu[order]
    return total 
    

def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("Your order is: ")
    # your code goes here!
    print("This is your order %s" % order_list)
    x= get_total_price(order_list)
    print("%0.3f KWD" % x)

