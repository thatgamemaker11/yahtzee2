
def score(section):
    ones = 0
    twos = 0
    threes = 0
    fours = 0
    fives = 0
    sixes = 0
    while True:
        if section == "ones":
            if ones == 0:
                ones = int(input("how many points to add to this section?"))
                break
            else:
                print("You already have a score here!")
        elif section == "twos":
            twos = int(input("how many points to add to this section?"))
        elif section == "threes":
            threes = int(input("how many points to add to this section?"))
        elif section == "fours":
            fours = int(input("how many points to add to this section?"))
        elif section == "fives":
            fives = int(input("how many points to add to this section?"))
        elif section == "sixes":
            sixes = int(input("how many points to add to this section?"))
#===    ===========================================================
