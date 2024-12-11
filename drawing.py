import turtle


t = turtle.Turtle('turtle')
t.hideturtle()

t.penup()
t.goto(100, 265)
t.pendown()
t.pencolor("yellow")
t.write("YAHTZEE!", move=False, align='center', font=('Arial', 70, 'bold'))
