import random
import dice


def dieRand(loc):
    list = [1, 2, 3, 4, 5, 6]
    num = random.choice(list)

    if num == 1:
        dice.one(loc)
        return 1
    elif num == 2:
        dice.two(loc)
        return 2
    elif num == 3:
        dice.three(loc)
        return 3
    elif num == 4:
        dice.four(loc)
        return 4
    elif num == 5:
        dice.five(loc)
        return 5
    elif num == 6:
        dice.six(loc)
        return 6
