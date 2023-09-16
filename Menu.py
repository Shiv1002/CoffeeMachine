class MenuItem:
    def __init__(self,name,water,milk,cost,coffee) -> None:
        self.name = name
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cost = cost


class Menu:
    def __init__(self) -> None:
        self.menu = [
            MenuItem(name = 'espresso',water = 30,milk = 120,coffee = 20, cost = 12),
            MenuItem(name = 'latte',water = 40,milk = 100,coffee = 30, cost = 10),
            MenuItem(name = 'cappa',water = 10,milk = 80, coffee = 25, cost = 20),
        ]
        

    def get_menu(self) -> None:
        items = ""
        index = 1
        for item in self.menu:
            items += f' {item.name} |'
            index+=1
        return items
    
    def find_drink(self,drink_name):

        for item in self.menu:
            if item.name  == drink_name:
                return item
            
        return None

# print(Menu().get_menu()) 
# espresso/latte/cappa/

# print(Menu().menu[0]) 

# print(vars(Menu().menu[0]))
