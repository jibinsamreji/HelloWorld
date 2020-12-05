class Point:
    # Constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


""" point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 12
print(point2.x)"""

point = Point(10, 20)
point.x = 11
print(point.x)


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


jibin = Person("Jibin Reji")
print(jibin.name)
jibin.talk()

bob = Person("Bob Smith")
bob.talk()
