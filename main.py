#imports
import card
import roll
import score
import drawing


#setting booleans
keep1 = "F"
keep2 = "F"
keep3 = "F"
keep4 = "F"
keep5 = "F"

#card
card.cardgif()
card.pointDraw(15,"99")

scale = 1.8

while True: #loop to keep the game going
    if keep1 == "F":
        die1 = roll.dieRand(-120*scale)
    if keep2 == "F":
        die2 = roll.dieRand(-70*scale)
    if keep3 == "F":
        die3 = roll.dieRand(-20*scale)
    if keep4 == "F":
        die4 = roll.dieRand(30*scale)
    if keep5 == "F":
        die5 = roll.dieRand(80*scale)

    for i in range(3):
        keep1 = input("Do you want to keep dice 1? (T/F) ").upper()
        keep2 = input("Do you want to keep dice 2? (T/F) ").upper()
        keep3 = input("Do you want to keep dice 3? (T/F) ").upper()
        keep4 = input("Do you want to keep dice 4? (T/F) ").upper()
        keep5 = input("Do you want to keep dice 5? (T/F) ").upper()


        if keep1 == "F":
            die1 = roll.dieRand(-120*scale)
        if keep2 == "F":
            die2 = roll.dieRand(-70*scale)
        if keep3 == "F":
            die3 = roll.dieRand(-20*scale)
        if keep4 == "F":
            die4 = roll.dieRand(30*scale)
        if keep5 == "F":
            die5 = roll.dieRand(80*scale)
        print("===================================================================")


    score.score(input("what section would you like to place you points in?"))
