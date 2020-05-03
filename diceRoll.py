import random
from pathlib import Path


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()
print(dice.roll())

path = Path("ecommerce")
print(path.exists())
pathS = Path()
print(pathS.glob('*.py'))

for file in pathS.glob('*.py'):
    print(file)

for file1 in pathS.glob('*'):
    print(file1)
