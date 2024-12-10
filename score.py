
def score(section):
    ones = 0
    twos = 0
    threes = 0
    fours = 0
    fives = 0
    sixes = 0
    while True:
        if section[0] == "O":
            ones = int(input("how many points to add to this section?"))
            break
        elif section == "twos":
            twos = int(input("how many points to add to this section?"))
            break
        elif section == "threes":
            threes = int(input("how many points to add to this section?"))
            break
        elif section == "fours":
            fours = int(input("how many points to add to this section?"))
            break
        elif section == "fives":
            fives = int(input("how many points to add to this section?"))
            break
        elif section == "sixes":
            sixes = int(input("how many points to add to this section?"))
            break
#===    ===========================================================
        elif section == "3 of a Kind":
            threeOFK = int(input("how many points to add to this section?"))
            break
        elif section == "4 of a Kind":
            fourOFK = int(input("how many points to add to this section?"))
            break
        elif section == "Full House":
            FullH = int(input("how many points to add to this section?"))
            break
        elif section == "Sm straight":
            Smstr = int(input("how many points to add to this section?"))
            break
        elif section == "Lg straight":
            Lgstr = int(input("how many points to add to this section?"))
            break
        elif section == "YAHTZEE":
            twos = int(input("how many points to add to this section?"))
            break
        elif section == "Chance":
            threes = int(input("how many points to add to this section?"))
            break
