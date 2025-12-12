class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def drive(self):
        print(f"Driving car ...")

class SportCar(Car):

    def insanely_fas_drive(self):
        print(f"Driving insanely fast...")

my_car = Car("Honda", "CR-V", 2008)
my_car.drive()
my_new_car = SportCar("Dodge", "Challenger", 2026)
my_new_car.insanely_fas_drive()

