#file: persegiempatturtle.py

import turtle

s = turtle.getscreen()
s.title("Belajar Turtle pada Python")
s.bgcolor("lightblue")
s.setup(width=300, height=200)

t = turtle.Turtle()

t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)

turtle.done()