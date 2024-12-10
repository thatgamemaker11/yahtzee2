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
    card.back(350)
    screen = Screen()
    screen.addshape("card cropped.gif")
    card.shapesize(stretch_wid=0.1, stretch_len=0.1, outline=None)

    card.shape("card cropped.gif")
def pointDraw(row):
    p = Turtle()
    p.right(90)
    p.forward(300)
    p.setheading(0)
    p.back(250)
    p.left(90)
    p.forward(20)
    p.forward(30*row*2)
