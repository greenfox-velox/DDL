from dice import *


class CharacterStats():
    def __init__(self):
        self.dices = Dice()

    def stats_boss(self):
        dices = self.dices.random_dice(5)
        level = 1
        HP = 2 * level  * dices[0] + dices[1]
        DP = 1 + dices[2]//2 + dices[3]//2
        SP = dices[4] + level
        return HP, DP, SP

    def stats_skeleton(self):
         dices = self.dices.random_dice(3)
         HP = 20 + dices[0]
         DP = dices[1]//2
         SP = dices[2]
         return HP, DP, SP

    def stats_hero(self):
         dices = self.dices.random_dice(3)
         HP = 20 + 3 * dices[0]
         DP = 2 * dices[1]
         SP = 5 + dices[2]
         return HP, DP, SP
