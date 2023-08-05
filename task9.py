"""
Implement a class Car with attributes: model, year, color.
Implement methods drive and get_info with placeholder pass.
Create a class DVSCar that inherits from the Car class.
Add attributes: tank (fuel tank) and engine.
Override the drive method to deduct fuel from the tank when driven.
Create a class ElectroCar that inherits from the Car class.
Add attributes: battery (default value 100) and electro_engine.
Override the drive method to deduct battery charge when driven.
Create a class HybridCar that inherits from both DVSCar and ElectroCar.
Override the drive method to enable consuming both fuel and battery charge.
"""

class Car():
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def get_info(self):
        return f"Model: {self.model}, Year: {self.year}, Color: {self.color}"

    def drive(self, distance):
        pass

class DVSCar(Car):
    def __init__(self, model, year, color, tank, engine):
        super().__init__(model, year, color)
        self.engine = 'engine'
        self.tank = tank

    def drive(self, fuel):
        if fuel <= self.tank:
            self.tank -= fuel
            print(f'Remaining fuel: {self.tank} liters')
        else:
            print('Insufficient fuel in the tank')

class ElectroCar(Car):
    def __init__(self, model, year, color, battery, electro_engine):
        super().__init__(model, year, color)
        self.battery = 100
        self.electro_engine = 'Electric engine'

    def drive(self, battery_percent):
        if battery_percent <= 100:
            self.battery -= battery_percent
            print(f"Remaining charge: {self.battery}%")
        else:
            print("Insufficient charge for the trip!")

class HybridCar(DVSCar, ElectroCar):
    def drive(self, fuel, battery_percent, engine=None):
        if engine == 'DVSCar':
            self.tank -= fuel
            print(f"Remaining fuel: {self.tank} liters")
        else:
            self.battery -= battery_percent
            print(f"Remaining charge: {self.battery}%!")

# Create objects and test methods
dvs_car = DVSCar('Toyota', 2023, 'blue', 50, 'V6')
dvs_car.drive(20)

electro_car = ElectroCar('Tesla', 2023, 'white', 80, 'Electric Motor')
electro_car.drive(30)

hybrid_car = HybridCar('Toyota-Tesla', 2023, 'gray', 40, 'V6 + Electric Motor')
hybrid_car.drive(15, 50)
