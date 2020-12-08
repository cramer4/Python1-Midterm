from random import randint
class Die:
    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        roll = randint(1, self.sides)
        print(roll)
    def roll_ten_times(self):
        for _ in range(0, 10):
            self.roll_die()

    def calculate_probability(self):
        probability = 1 / self.sides
        print(probability)

my_die = Die(6)
my_die.roll_ten_times()
my_die.calculate_probability()