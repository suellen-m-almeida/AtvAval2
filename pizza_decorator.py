
class PizzaComponent: #Componente
    def getDescription(self):
        return self.__class__.__name__

    def getTotalCost(self):
        return self.__class__.cost


class BasePizza(PizzaComponent): #ComponenteConcreto
    cost = 0.00  # custo base da pizza


class Decorator(PizzaComponent): #Decorador
    def __init__(self, pizzaComponent):
        self.component = pizzaComponent

    def getTotalCost(self):
        return self.component.getTotalCost() + PizzaComponent.getTotalCost(self)

    def getDescription(self):
        return self.component.getDescription() + ' ' + PizzaComponent.getDescription(self)


class Cheese(Decorator):
    cost = 1.25
    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)

class Ham(Decorator):
    cost = 1.00
    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)
        
class Pepperoni(Decorator):
    cost = 1.50
    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)

class Chicken(Decorator):
    cost = 2.50
    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)

class Olives(Decorator):
    cost = 0.75
    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)

class Tomato(Decorator):
    cost = 0.50
    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)

class Basil(Decorator):
    cost = 0.50
    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)

class GuavaPaste(Decorator):
    cost = 0.50
    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)

class Chocolate(Decorator):
    cost = 2.00
    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)

class Strawberry(Decorator):
    cost = 0.75
    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)

# ChickenAndCheese = Chicken(Cheese(BasePizza()))
# print( ChickenAndCheese.getDescription() + ": $" + str(ChickenAndCheese.getTotalCost()) )