'''Create a class called Wallet. Override the dunder methods __add__ and __sub__. 
The class should have an attribute self.balance. When using the + operator, the amount should 
be added to the balance. If the added amount is negative, an error should be raised. When using 
the - operator, subtract the amount from the balance. 
When printing the object, it should display the current balance. Override the __str__ method.'''

class Wallet:
    def __init__(self, balance):
        self.balance = balance

    def __add__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError('Numeric value required!')
        if other < 0:
            raise ValueError('Number must be positive!')
        self.balance += other

    def __sub__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError('Numeric value required!')
        if other < 0:
            raise ValueError('Number must be positive!')
        if other > self.balance:
            raise ValueError('You don\'t have enough balance!')
        self.balance -= other

    def __str__(self):
        return f'Your balance is: {self.balance}$'

wallet1 = Wallet(5000)
wallet1 + 300  # Add 300 to balance
print(wallet1)

wallet1 - 800  # Subtract 800 from balance
print(wallet1)
