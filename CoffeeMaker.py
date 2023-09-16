# make coffe maker model
class Coffee_maker:
    def __init__(self):
        self.resource = {
            "water":100,
            "milk":100,
            "coffee":100,
        }
    

    def report(self):
        print(f"Water : {self.resource['water']}ml")
        print(f"Milk : {self.resource['milk']}ml")
        print(f"Coffee : {self.resource['coffee']}g")
    
    def isSufficient(self,drink):
        can_make = True
        #  make drink iterable 
        for item in drink:
            if item in self.resource and drink[item] > self.resource[item]:
                print(f"Sorry there is not enought {item}")
                can_make = False
                break
        return can_make
    

    def make_order(self, order):
        for item in order:
            if item in self.resource:
                self.resource[item] -= order[item]

        print(f"Here is your {order['name']} ☕")


# print(Coffee_maker())