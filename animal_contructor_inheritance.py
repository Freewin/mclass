import random


class Animal(object):

    def __init__(self, name):
        self.name = name


class Dog(Animal):

    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.breed = random.choice(["Shih Tsu", "Beagle", "Mutt"])

    def fetch(self, thing):
        print (f"{self.name} goes after the {self.thing}")


d = Dog("mydog")

print(d.name)
print(d.breed)