class Wheels:
    def __init__(self, count):
        self.count = count

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

class Doors:
    def __init__(self, count):
        self.count = count

class Car(Wheels, Engine, Doors):
    def __init__(self, wheels_count, horsepower, doors_count):
        Wheels.__init__(self, wheels_count)
        Engine.__init__(self, horsepower)
        Doors.__init__(self, doors_count)

    def info(self):
        return f"Авто с {self.count} колёсами, двигатель мощностью {self.horsepower} л.с., и {self.count} двери."

my_car = Car(4, 150, 4)
print(my_car.info())