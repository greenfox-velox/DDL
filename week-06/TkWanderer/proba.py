from random import randint

def random_dice(times):
    dice = []
    for i in range(times):
        i = randint(1,6)
        dice.append(i)
    return dice

print(random_dice(3))


def stats_hero():
    dice = random_dice(3)
    HP = 20 + 3 * int(dice[0])
    DP = 2 * int(dice[1])
    SP = 5 + int(dice[2])
    return HP, DP, SP

print(stats_hero())


def stats_skeleton():
    dice = random_dice(3)
    HP = 20 + int(dice[0])
    DP = int(dice[1])//2
    SP = int(dice[2])
    return HP, DP, SP

print(stats_skeleton())


def stats_boss():
    dice = random_dice(5)
    level = 1
    HP = 2 * level * int(dice[0]) + int(dice[1])
    DP = int(dice[2])//2 + int(dice[3])//2
    SP = int(dice[4]) + level
    return HP, DP, SP

print(stats_boss())
