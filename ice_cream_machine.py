class IceCreamMachine:
    
    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings
        
    def scoops(self):
        l = []
        for ingredient in self.ingredients:
            for topping in self.toppings:
                l.append([ingredient, topping])
        return l

if __name__ == "__main__":
    machine = IceCreamMachine(["vanilla", "chocolate", "strawberry"], ["sprinkles"])
    print(machine.scoops()) 