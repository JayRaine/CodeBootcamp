from turtle import Turtle
from random import randint

jay = Turtle()

jay.color('red')
jay.shape('turtle')

jay.penup()
jay.goto(-160, 100)
jay.pendown()

ivo = Turtle()

ivo.color("green")
ivo.shape("turtle")

ivo.penup()
ivo.goto(-160, 70)
ivo.pendown()

liam = Turtle()

liam.color("blue")
liam.shape("turtle")

liam.penup()
liam.goto(-160, 40)
liam.pendown()



for movement in range(100):
    jay.forward(randint(1, 5))
    ivo.forward(randint(1, 5))
    liam.forward(randint(1, 5))

input("Press Enter to close")
