'''
Create a class Product with attributes:

name - product name.
price - product price.
satiety_count - satiety value the product provides upon consumption.
No methods are required for this class.

Create a class Person with attributes:

name - name.
cash (protected) - amount of money.
debt (private) - debt (default: 0).
satiety - satiety level (default: 100, can go above).
salary - salary (default value of your choice).
Methods for the Person class:

work(self): The person can work and earn money based on their salary. It also decreases the satiety 
by 40 units.
get_cash_status(self): Returns the amount of money the person has.
get_debt(self, sum): Allows the person to take money as a debt, adding the specified amount 
to the debt attribute.
get_debt_status(self): Displays the person's debt status. If the debt exceeds their available cash, 
it should print "Bankrupt!".
get_satiety_status(self): Prints information about the person's satiety. If it goes below 20, 
a warning is printed. If it goes below 0, the person dies.
buy_and_eat(self, product): The person can buy and eat a product (an object of the Product class
described below). The product has a satiety_count attribute that adds to the person's satiety. 
The product also has a price attribute that is deducted from the person's cash. If the person doesn't 
have enough money, they cannot buy the product.
'''

class Product():
  def __init__(self,name,price,satiety_count):
    self.name=name
    self.price=price
    self.satiety_count=satiety_count


class Person():
   
    def __init__(self,name,cash):
        self.name=name
        self._cash=cash
        self.__debt=0
        self.satiety=100
        self.salary=20000


    def work(self):
        self._cash+=self.salary
        self.satiety-=40
        print(f'Ваша зарплата составляет: {self.salary}$,на вашем счету: {self._cash}$. Ваш коэффициент сытости составляет: {self.satiety}единиц')
    def get_status_cash(self):
        print(f'На вашем счету: {self._cash}$')
    def get_debt(self,sum):
        self.__debt+=sum
        print(f'Вы взяли в долг {sum}$')
    def get_debt_status(self):
        if self.__debt>self._cash:
            print('Ваш кредит превышает дебет! Вы банкрот!')
        else:
            print(f'Ваш долг составляет {self.__debt}$')
    def get_satiety_status(self):
        if self.satiety<20:
            print('Ваш коэффициент сытости близится к нулю. Просьба пополнить его')
        elif self.satiety<=0:
            print(f'{self.name} умер')
        else:
            print(f'Ваш коэффициент сытости составляет: {self.satiety} единиц')
       
    def buy_and_eat(self,product):
        if isinstance(product,Product):
            if self._cash>=product.price:
                self._cash-=product.price
                self.satiety+=product.satiety_count
                print(f'Вы купили {product.name}')
            else:
                print(f'У вас недостаточно денег для купли {self.product}')
        else:
            raise ValueError('Объект не является классом Product')
 
     
product=Product('арбуз',3,40)
human=Person('Aizhanyl',10000)
human.work()
human.get_status_cash()
human.get_debt(100)
human.get_debt_status()
human.get_satiety_status()
human.buy_and_eat(product)