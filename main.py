from turtle import *


def half_circle(t1, t2, rang):
    for i in range(60):
        t1.forward(rang)
        t2.forward(rang)
        t1.right(3)
        t2.right(3)

def dance(t1, t2, rang):
    for i in range(60):
        t1.forward(rang)
        t2.forward(rang)
        t1.right(3)
        t2.right(3)
        if i % 30 == 0:
            for j in range(20):
                t1.right(18)
                t2.right(18)


def love_heart(t1, t2):
    t1.begin_fill()
    t2.begin_fill()
    for i in range(70):
        t1.forward(4)
        t2.forward(4)
        t1.right(3)
        t2.left(3)
    for i in range(58):
        t1.forward(5)
        t2.forward(5)
    t1.end_fill()
    t2.end_fill()


vadik = Turtle()
viola = Turtle()
vadik.shape('circle')
viola.shape('circle')
vadik.color('blue')
viola.color('pink')
vadik.penup()
viola.penup()
vadik.speed(0)
viola.speed(0)
vadik.pensize(5)
viola.pensize(5)
viola.left(180)

half_circle(vadik, viola, 4)
vadik.pendown()
viola.pendown()
vadik.shape('triangle')
viola.shape('triangle')
half_circle(vadik, viola, 8)
vadik.shape('turtle')
viola.shape('turtle')
dance(vadik, viola, 8)
vadik.pensize(2)
viola.pensize(2)
dance(vadik, viola, 4)


viola.clear()
vadik.clear()
vadik.left(90)
viola.right(90)
vadik.pensize(10)
viola.pensize(10)
love_heart(vadik, viola)
vadik.hideturtle()
viola.hideturtle()

exitonclick()
