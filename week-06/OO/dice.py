from random import randint

class Dice():
    def random_dice(self, number_of_throws):
        dice = []
        for i in range(number_of_throws):
            i = randint(1,6)
            dice.append(i)
        return dice
