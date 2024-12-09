import card
import roll
import score



keep1 = "F"
keep2 = "F"
keep3 = "F"
keep4 = "F"
keep5 = "F"
#card.card()
while True:
    if keep1 == "F":
        die1 = roll.dieRand(-120)
    if keep2 == "F":
        die2 = roll.dieRand(-70)
    if keep3 == "F":
        die3 = roll.dieRand(-20)
    if keep4 == "F":
        die4 = roll.dieRand(30)
    if keep5 == "F":
        die5 = roll.dieRand(80)

    for i in range(3):
        keep1 = input("Do you want to keep dice 1? (T/F) ").upper()
        keep2 = input("Do you want to keep dice 2? (T/F) ").upper()
        keep3 = input("Do you want to keep dice 3? (T/F) ").upper()
        keep4 = input("Do you want to keep dice 4? (T/F) ").upper()
        keep5 = input("Do you want to keep dice 5? (T/F) ").upper()


        if keep1 == "F":
            die1 = roll.dieRand(-120)
        if keep2 == "F":
            die2 = roll.dieRand(-70)
        if keep3 == "F":
            die3 = roll.dieRand(-20)
        if keep4 == "F":
            die4 = roll.dieRand(30)
        if keep5 == "F":
            die5 = roll.dieRand(80)


    score.score(input("what section would you like to place you points in?"))
