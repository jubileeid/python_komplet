#file: dotturtle.py

import turtle

s = turtle.getscreen()
s.title("Belajar Turtle pada Python")
s.bgcolor("lightblue")
s.setup(width=300, height=200)

t = turtle.Turtle()

t.dot(100)

turtle.done()