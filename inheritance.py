class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    pass


class Cat(Mammal):
    def cat_action(self):
        print("Annoying")


# pass to deal empty class


"""Duplicate here:
class Cat:
    def walk(self):
        print("walk")
"""

dog1 = Dog()
dog1.walk()

cat1 = Cat()
cat1.cat_action()

