import turtle

t = turtle.Turtle()

# Mengatur ketebalan pena ke berbagai nilai
t.pensize(1)
t.forward(100)

t.penup()
t.goto(-150, 50)
t.pendown()

t.pensize(10)
t.forward(100)

t.penup()
t.goto(-150, 100)
t.pendown()

t.pensize(20)
t.forward(100)

turtle.done()
