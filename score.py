import card

def score(section):
    ones = 0
    twos = 0
    threes = 0
    fours = 0
    fives = 0
    sixes = 0
    while True:
        if section[0] == "o":
            ones = input("How many points to add to this section?")
            card.pointDraw(26, ones)
            break
        elif section == "twos":
            twos = input("How many points to add to this section?")
            card.pointDraw(26, ones)
            break
        elif section == "threes":
            threes = input("How many points to add to this section?")
            card.pointDraw(26, ones)
            break
        elif section == "fours":
            fours = input("How many points to add to this section?")
            card.pointDraw(26, ones)
            break
        elif section == "fives":
            fives = input("How many points to add to this section?")
            card.pointDraw(26, ones)
            break
        elif section == "sixes":
            sixes = input("How many points to add to this section?")
            card.pointDraw(26, ones)
            break
#===    ===========================================================
        elif section == "3 of a Kind":
            threeOFK = input("How many points to add to this section?")
            break
        elif section == "4 of a Kind":
            fourOFK = input("How many points to add to this section?")
            break
        elif section == "Full House":
            FullH = input("How many points to add to this section?")
            break
        elif section == "Sm straight":
            Smstr = input("How many points to add to this section?")
            break
        elif section == "Lg straight":
            Lgstr = input("How many points to add to this section?")
            break
        elif section == "YAHTZEE":
            twos = input("How many points to add to this section?")
            break
        elif section == "Chance":
            threes = input("How many points to add to this section?")
            break
        elif section == "YAHTZEE Bonus":
            threes = input("How many points to add to this section?")
            break