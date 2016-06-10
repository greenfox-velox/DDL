from random import randint

class Dice():
    def random_dice(self, number_of_throws):
        dice = []
        for i in range(number_of_throws):
            i = randint(1,6)
            dice.append(i)
        return dice

dice = Dice()
print(dice.random_dice(3))

dice2 = Dice()
print(dice.random_dice(5))
