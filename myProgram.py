# Q2
class Vehicle:
    pass


# Q3
class Vehicle:
    engine_capacity = "1.6 Turbo"


# Q4
class Vehicle:
    def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tank = type_of_tank
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity

    def drive(self):
        print("The vehicle is in driving mode now.")


# Q5
vios = Vehicle('4', 'petrol', 5, 180)
print(vios.number_of_wheels)
print(vios.type_of_tank)
print(vios.seating_capacity)
print(vios.maximum_velocity)

# Q6
vios.drive()


# Q7
class ElectricCar(Vehicle):
    def __init__(self, number_of_wheels, seating_capacity, maximum_velocity):
        Vehicle.__init__(self, number_of_wheels, 'electric', seating_capacity, maximum_velocity)


# Q8
blueSG = ElectricCar('4', 5, 150)
blueSG.drive()


# Q10
class Computer:
    def __init__(self, device_name, screen_size, processor, ram):
        self.device_name = device_name
        self.screen_size = screen_size
        self.processor = processor
        self.ram = ram

    def playGame(self, parameter1, parameter2):
        print("You are playing", parameter1, "and", parameter2, "on the", self.device_name)


class laptop(Computer):
    def __init__(self, screen_size, processor, ram):
        Computer.__init__(self, "laptop", screen_size, processor, ram)


class desktop(Computer):
    def __init__(self, screen_size, processor, ram):
        Computer.__init__(self, 'desktop', screen_size, processor, ram)


desktop = desktop("15 inch", "intel (R)", "8GB")
desktop.playGame("LOL", "CSGO")
laptop = laptop("13 inch", "intel (R)", "16GB")
laptop.playGame("DOTA2", "Minecraft")