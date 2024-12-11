from turtle import *
def card():
  print("""
  | UPPER SECTION | HOW TO SCORE | GAME |
  =======================================
  |    ONES       |    COUNT     |      |
  |               |  ONES ONLY   |      |
  =======================================
  |    TWOS       |    COUNT     |      |
  |               |  TWOS ONLY   |      |
  =======================================
  |    THREES     |    COUNT     |      |
  |               |  THREES ONLY |      |
  =======================================
  |    FOURS      |    COUNT     |      |
  |               |  FOURS ONLY  |      |
  =======================================
  |    FIVES      |    COUNT     |      |
  |               |  FIVES ONLY  |      |
  =======================================
  |    SIXES      |    COUNT     |      |
  |               |  SIXES ONLY  |      |
  =======================================
  =======================================
  |    TOTAL      |   ____ \     |      |
  |    SCORE      |   ‾‾‾‾ /     |      |
  =======================================
  |    BONUS      |    SCORE     |      |
  |    SCORE      |     35       |      |
  =======================================
  |    TOTAL      |   ____ \     |      |
  |               |   ‾‾‾‾ /     |      |
  =======================================
  +++++++++++++LOWER SECTION+++++++++++++
  =======================================
  |    3 OF A     |   ADD TOTAL  |      |
  |     KIND      |  OF ALL DICE |      |
  =======================================
  |    4 OF A     |   ADD TOTAL  |      |
  |     KIND      |  OF ALL DICE |      |
  =======================================
  |     FULL      |     SCORE    |      |
  |     HOUSE     |      25      |      |
  =======================================
  |       SM      |     SCORE    |      |
  |     STRAIGHT  |      30      |      |
  =======================================
  |   YAHTZEE!!   |     SCORE    |      |
  |               |      50      |      |
  =======================================
  |     CHANCE    |     ALL      |      |
  |               |     DICE     |      |
  =======================================
  |    YAHTZEE    |     SCORE    |      |
  |     BONUS     |    100 PER   |      |
  =======================================
  =======================================
  |    UPPER      |   ____ \     |      |
  |    TOTAL      |   ‾‾‾‾ /     |      |
  =======================================
  |    LOWER      |   ____ \     |      |
  |    TOTAL      |   ‾‾‾‾ /     |      |
  =======================================
  |    GRAND      |   ____ \     |      |
  |    TOTAL      |   ‾‾‾‾ /     |      |
  =======================================
  """)

def cardgif():
    card = Turtle()
    card.penup()
    card.back(320)
    screen = Screen()
    screen.addshape("carddd.gif")
    card.shapesize(stretch_wid=0.1, stretch_len=0.1, outline=None)

    card.shape("carddd.gif")
def pointDraw(row,score):
    p = Turtle()
    p.penup()
    p.hideturtle()
    p.goto(-205,-336)
    p.setheading(90)

    p.forward(26*row-30)
    p.write(score, font=("Arial", 14, "normal"),align="center")
