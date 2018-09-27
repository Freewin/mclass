# Demonstrate inheritance using a base class
# and multiple subclasses that inherit from
# parent


class Animal(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(f"{self.name} is eating {food}")


class Dog(Animal):
    def fetch(self, thing):
        print(f"{self.name} goes after the {thing}")


class Cat(Animal):
    def swatstring(self):
        print(f"{self.name} shreds the string!")


r = Dog("Rover")
f = Cat("Fluffy")

r.fetch("paper")
f.swatstring()
r.eat("dog food")
f.eat("cat food")
