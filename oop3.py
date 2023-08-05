'''

Create classes called Hero and Soldier.

Class Hero should have attributes: name, damage, and soldiers=[].
Class Soldier should have attributes: name, damage, and captain 
(which should be an object of class Hero).

A Hero should have a method to add new soldiers to their squad, add_soldier.
For a soldier, add a method change_captain(new_captain) which should change 
the captain of that soldier and can only be called within the add_soldier method of the Hero class.

Additional (Optional):

Add fields for storing the direction of the squad for both Soldier and Hero.
Add a method for the Hero class to change the direction. When the hero changes direction, 
the entire squad should change direction.
Possible directions: North, South, East, West.
It's important to note that a soldier cannot change their own squad. Only a hero can add a soldier to 
their squad and remove a soldier from their squad.'''

class Hero:
    def __init__(self, name, damage, direction):
        self.name = name
        self.damage = damage
        self.direction = direction
        self.soldiers = []
       
    def add_soldier(self, soldier):
        if isinstance(soldier, Soldier):
            if soldier not in self.soldiers:
                self.soldiers.append(soldier)
                print(f'Soldier {soldier} added to the squad')
                soldier.change_captain(self)
            else:
                print(f'{soldier} is already in the squad')
        else:
            raise ValueError('Object must be a soldier')
           
    def change_direction(self, new_direction):
        for soldier in self.soldiers:
            print(f'{self.name} is heading {self.direction}')
            soldier.change_direction(new_direction)
            print(f'The squad changed direction from {self.direction} to {new_direction}')
        self.direction = new_direction
   
   
class Soldier:
    def __init__(self, name, damage, captain, direction):
        self.name = name
        self.damage = damage
        self.direction = direction
        self.captain = captain
       
    def change_captain(self, new_captain):
        self.captain = new_captain
        print(f'{new_captain.name} is now the captain of {self.name}')
       
    def change_direction(self, new_direction):
        self.direction = new_direction

    def __repr__(self):
        return f'{self.name}'
   
hero = Hero('Alex', 40, 'North')
soldier1 = Soldier('Vyacheslav', 30, 'Cryuc', 'West')
hero.add_soldier(soldier1)
hero.change_direction('South')
hero.change_direction('West')
hero1 = Hero('Alx', 40, 'North')
soldier1.change_captain(hero1)
hero1.change_direction('West')
print(soldier1.direction)
soldier1.change_captain(hero)
hero.add_soldier(soldier1)
