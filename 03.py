class Pet:
    def __init__(self, name, type_name):
        self.name = name
        self.type_name = type_name

    def sound(self):
        raise NotImplementedError("Метод должен быть предопределён.")

    def show(self):
        print(f"Имя моего питомца: {self.name}")

    def type(self):
        print(f"Это {self.type_name}")

class Dog(Pet):
    def __init__(self, name):
        super().__init__(name, "Собака")

    def sound(self):
        print("Гав!")

class Cat(Pet):
    def __init__(self, name):
        super().__init__(name, "Кот")

    def sound(self):
        print("Мяу!")

class Parrot(Pet):
    def __init__(self, name):
        super().__init__(name, "Попугай")

    def sound(self):
        print("Чирик!")

class Hamster(Pet):
    def __init__(self, name):
        super().__init__(name, "Хомяк")

    def sound(self):
        print("Пищ!")

pets= [Dog("Барбос"), Cat("Саймон"), Parrot("Аркаша"), Hamster("Хома")]

for pet in pets:
    pet.show()
    pet.sound()
    pet.type()
    print()
