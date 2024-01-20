def shopping_cart():
    def print_cart(cart):
        if cart == {}:
            print("There are no items in your cart.")
        else:
            print("-----------------------")
            print("Your Shopping Cart:")
            for item, quantity in cart.items():
                print(f"{quantity} {item}")

    def add_remove(operation):
        while True:
            item = input(f"What type of item would you like to {operation}?").strip().lower()
            if item == 'quit':
                return 0
            elif item == 'go back':
                return
            elif item.isalpha():
                if item not in cart.keys():
                    if operation == 'remove':
                        print(f"There are no {item} in your cart to remove.")
                        return
                    cart[item] = 0         
                print(f"You currently have {cart[item]} {item} in your cart")
                while True:
                    quantity = input(f"How many {item} would you like to {operation}?").strip()
                    if quantity == 'quit':
                        return 0
                    elif quantity == 'go back':
                        break
                    elif quantity.isdigit() and int(quantity) > 1:
                        if operation == 'add':
                            cart[item] += int(quantity)
                        elif operation == 'remove':
                            cart[item] -= int(quantity)
                            if cart[item] < 1:
                                del cart[item]
                        try:
                            print(f"You now have {cart[item]} {item} in your cart")
                        except:
                            print(f"You have removed all of the {item} from your cart.")
                        return
                    else:
                        print("Please enter the quantity in positive whole digits.")
            else:
                print(f"Please enter the name of the item you would like to {operation}. Or type 'go back' to choose a different action.")
                
    cart = {}
    print("Welcome to your Shopping Cart!")
    while True:
        result = int
        action = input("What would you like to do? Add, Show, Remove, or Quit").strip().lower()
        if action not in ['add','show','remove','quit']:
            print("I didn't get that. Please type one of these actions for your Shopping Cart: Add, Show, Remove, or Quit")
        if action == 'quit':
            break
        elif action == 'show':
            print_cart(cart)
        elif action == 'add':
            result = add_remove('add')
        elif action == 'remove':
            result = add_remove('remove')
        if result == 0:
            return
    print_cart(cart)
    return print("\n ----------------- \n Goodbye!")
            

shopping_cart()