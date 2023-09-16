from CoffeeMaker import Coffee_maker
from Menu import Menu
from PayMachine import Pay_machine
coffee_machine = Coffee_maker()
menu = Menu()
pay_machine = Pay_machine()

while True:
    all_menu_items_in_string = menu.get_menu()
    user_choice = input(f"Type REPORT to get the resource report as of now\n"+
                        f"Type OFF turn off the machine\n"+
                        f"​What would you like? {all_menu_items_in_string}\n")
    menu_items = menu.menu
    # print(menu_items)

    if user_choice == 'off':
        break
    elif user_choice == 'REPORT':
        coffee_machine.report()
    else:
        drink  = menu.find_drink(user_choice)
        if drink == None:
            print(f"\nFind drink those are available in menu!!!\n")
            continue
        
        # make  drink object iterable
        drink = vars(drink)

        if coffee_machine.isSufficient(drink):
            payment = pay_machine.process_coins()
            if pay_machine.is_transaction_successful(payment, drink['cost']):
                coffee_machine.make_order(drink)
                
    
    




