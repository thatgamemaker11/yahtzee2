import turtle

t = turtle.Turtle('turtle')
scale = 3
turtle.bgcolor("red")
t.hideturtle()

t.speed(0)
t.width(int(10 / scale))
t.setheading(0)
t.width(int(10 / scale))


def one(loc):
    t.penup()

    t.setheading(0)
    t.width(int(10 / scale))
    t.goto(loc, 50)
    t.pendown()

    t.fillcolor("white")
    t.begin_fill()
    for i in range(4):
        t.forward(100 / scale)
        t.left(90)
    t.end_fill()

    t.penup()
    t.left(90)
    t.forward(50 / scale)
    t.right(90)
    t.forward(50 / scale)
    t.pendown()
    t.width(int(20 / scale))
    t.forward(.01)


def two(loc):
    t.penup()
    t.goto(loc, 50)
    t.pendown()

    t.width(int(10 / scale))
    t.setheading(0)
    t.pendown()

    t.fillcolor("white")
    t.begin_fill()
    for _ in range(4):
        t.forward(100 / scale)
        t.left(90)
    t.end_fill()

    t.penup()
    t.left(90)
    t.forward(70 / scale)
    t.right(90)
    t.forward(30 / scale)
    t.pendown()
    t.width(int(20 / scale))
    t.forward(.01)

    t.penup()
    t.forward(40 / scale)
    t.right(90)
    t.forward(40 / scale)
    t.pendown()
    t.width(int(20 / scale))
    t.forward(.01)


def three(loc):
    t.penup()

    t.goto(loc, 50)
    t.width(int(10 / scale))
    t.setheading(0)
    t.pendown()

    t.fillcolor("white")
    t.begin_fill()
    for _ in range(4):
        t.forward(100 / scale)
        t.left(90)
    t.end_fill()

    t.penup()
    t.left(90)
    t.forward(75 / scale)
    t.right(90)
    t.forward(25 / scale)
    t.pendown()
    t.width(int(20 / scale))
    t.forward(.01)

    t.penup()
    t.forward(25 / scale)
    t.right(90)
    t.forward(25 / scale)
    t.pendown()
    t.width(int(20 / scale))
    t.forward(.01)

    t.penup()
    t.left(90)
    t.forward(25 / scale)
    t.right(90)
    t.forward(25 / scale)
    t.pendown()
    t.width(int(20 / scale))
    t.forward(.01)


def four(loc):
    t.penup()
    t.goto(loc, 50)

    t.width(int(10 / scale))
    t.setheading(0)
    t.pendown()

    t.fillcolor("white")
    t.begin_fill()
    for _ in range(4):
        t.forward(100 / scale)
        t.left(90)
    t.end_fill()

    t.penup()
    t.left(90)
    t.forward(70 / scale)
    t.right(90)
    t.forward(30 / scale)
    t.pendown()
    t.width(int(20 / scale))
    t.forward(.01)

    t.penup()
    t.forward(40 / scale)
    t.right(90)
    t.forward(40 / scale)
    t.pendown()
    t.width(int(20 / scale))
    t.forward(.01)

    t.penup()
    t.right(90)
    t.forward(40 / scale)
    t.pendown()
    t.width(int(20 / scale))
    t.forward(.01)

    t.penup()
    t.right(90)
    t.forward(40 / scale)
    t.right(90)
    t.forward(40 / scale)
    t.pendown()
    t.width(int(20 / scale))
    t.forward(.01)


def five(loc):
    t.penup()

    t.goto(loc, 50)
    t.width(int(10 / scale))
    t.setheading(0)
    t.pendown()

    t.fillcolor("white")
    t.begin_fill()
    for _ in range(4):
        t.forward(100 / scale)
        t.left(90)
    t.end_fill()

    t.penup()
    t.left(90)
    t.forward(70 / scale)
    t.right(90)
    t.forward(30 / scale)
    t.pendown()
    t.width(int(20 / scale))
    t.forward(.01)

    t.penup()
    t.forward(40 / scale)
    t.right(90)
    t.forward(40 / scale)
    t.pendown()
    t.width(int(20 / scale))
    t.forward(.01)

    t.penup()
    t.right(90)
    t.forward(40 / scale)
    t.pendown()
    t.width(int(20 / scale))
    t.forward(.01)

    t.penup()
    t.right(90)
    t.forward(40 / scale)
    t.right(90)
    t.forward(40 / scale)
    t.pendown()
    t.width(int(20 / scale))
    t.forward(.01)

    t.penup()
    t.right(90)
    t.forward(20 / scale)
    t.right(90)
    t.forward(20 / scale)
    t.pendown()
    t.width(int(20 / scale))
    t.forward(.01)


def six(loc):
    t.penup()

    t.goto(loc, 50)
    t.width(int(10 / scale))
    t.setheading(0)
    t.pendown()

    t.fillcolor("white")
    t.begin_fill()
    for _ in range(4):
        t.forward(100 / scale)
        t.left(90)
    t.end_fill()

    t.penup()
    t.left(90)
    t.forward(75 / scale)
    t.right(90)
    t.forward(30 / scale)
    t.pendown()
    t.width(int(20 / scale))
    t.forward(.01)

    t.penup()
    t.right(90)
    t.forward(26 / scale)
    t.pendown()
    t.width(int(20 / scale))
    t.forward(.01)

    t.penup()
    t.forward(26 / scale)
    t.right(90)
    t.pendown()
    t.width(int(20 / scale))
    t.forward(.01)

    t.penup()
    t.right(90)
    t.forward(53 / scale)
    t.right(90)
    t.forward(38 / scale)
    t.pendown()
    t.width(int(20 / scale))
    t.forward(.01)

    t.penup()
    t.right(90)
    t.forward(26 / scale)
    t.pendown()
    t.width(int(20 / scale))
    t.forward(.01)

    t.penup()
    t.forward(26 / scale)
    t.right(90)
    t.pendown()
    t.width(int(20 / scale))
    t.forward(.01)
