'''
Create a class CoffeeMachine.

Add attributes: coffee_count, milk_count, sugar_count, and water_count, 
each with a maximum value of 100.

Create the following methods:

add_coffee(): Adds coffee to the machine. Should increase the coffee count.
add_sugar(): Adds sugar to the machine.
add_water(): Adds water to the machine.
add_milk(): Adds milk to the machine.
If adding any ingredient exceeds 100, prevent the addition.

make_coffee(): Prepares coffee using the available ingredients. The coffee requires specific amounts 
of each ingredient: coffee (30g), milk (40g), sugar (30g), and water (80g).
'''

class CoffeeMachine():
    def __init__(self, coffee_count, milk_count, sugar_count, water_count):
        values = [value for value in locals().values() if type(value) in (int, float)]
        for i in values:
            if i > 100 or i < 0:
                raise ValueError('Ingredient amounts should be between 0 and 100 grams')
        self.coffee_count = coffee_count
        self.milk_count = milk_count
        self.sugar_count = sugar_count
        self.water_count = water_count
     
    def add_coffee(self, gramm):
        difference = 100 - self.coffee_count
        if self.coffee_count + gramm <= 100 and 0 < gramm <= difference:
            self.coffee_count += gramm
            print('Coffee added')
        elif gramm > difference:
            print(f"You added too much coffee. The amount of coffee should not exceed {difference} grams.")
        else:
            print('You did not add coffee')
            
    def add_milk(self, gramm):
        difference = 100 - self.milk_count
        if self.milk_count + gramm <= 100 and 0 < gramm <= difference:
            self.milk_count += gramm
            print('Milk added')
        elif gramm > difference:
            print(f'You added too much milk. The amount of milk should not exceed {difference} grams.')
        else:
            print('You did not add milk')
            
    def add_sugar(self, gramm):
        difference = 100 - self.sugar_count
        if self.sugar_count + gramm <= 100 and 0 < gramm <= difference:
            self.sugar_count += gramm
            print('Sugar added')
        elif gramm > difference:
            print(f"You added too much sugar. The amount of sugar should not exceed {difference} grams.")
        else:
            print('You did not add sugar')
            
    def add_water(self, gramm):
        difference = 100 - self.water_count
        if self.water_count + gramm <= 100 and 0 < gramm <= difference:
            self.water_count += gramm
            print('Water added')
        elif gramm > difference:
            print(f'You added too much water. The amount of water should not exceed {difference} grams.')
        else:
            print('You did not add water')
                  
    def make_coffee(self):
        can_make_coffee = True
        if self.coffee_count < 30:
            print('You are out of coffee!')
            can_make_coffee = False
        if self.milk_count < 40:
            print('You are out of milk!')
            can_make_coffee = False
        if self.sugar_count < 30:
            print('You are out of sugar!')
            can_make_coffee = False
        if self.water_count < 80:
            can_make_coffee = False
            print('You are out of water!')
       
        if can_make_coffee:
            self.coffee_count -= 30
            self.milk_count -= 40
            self.sugar_count -= 30
            self.water_count -= 80
            print('Your coffee is ready! Enjoy!')

# Creating an instance of CoffeeMachine
coffee = CoffeeMachine(25, 35, 90, 25)

# Adding ingredients
coffee.add_coffee(30)
coffee.add_milk(25)
coffee.add_sugar(10)
coffee.add_water(75)

# Making coffee
coffee.make_coffee()
