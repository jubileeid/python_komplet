import turtle

s = turtle.getscreen()
s.title("Belajar Turtle pada Python")
s.bgcolor("lightblue")
s.setup(width=300, height=200)

t = turtle.Turtle()

t.right(90)
t.forward(100)
t.left(90)
t.backward(100)


turtle.done()