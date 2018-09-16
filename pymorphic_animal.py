class Animal(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(f"{self.name} is eating {food}")


class Dog(Animal):
    def fetch(self, thing):
        print(f"{self.name} goes after the {thing}")

    def show_affection(self):
        print (f"{self.name} wags tail")


class Cat(Animal):
    def swatstring(self):
        print(f"{self.name} shreds the string!")

    def show_affection(self):
        print (f"{self.name} purrs")


for a in (Dog("Rover"), Cat("Fluffy"), Cat("Meowers"), Dog("Scout")):
    a.show_affection()