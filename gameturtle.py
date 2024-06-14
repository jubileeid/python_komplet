import turtle
import random

# Setup jendela
wn = turtle.Screen()
wn.title("Game Tangkap Kura-kura")
wn.bgcolor("lightblue")
wn.setup(width=600, height=600)

# Membuat objek kura-kura
t = turtle.Turtle()
t.shape("turtle")
t.color("green")
t.penup()
t.speed(0)

# Skor
score = 0

# Fungsi untuk memindahkan kura-kura ke posisi acak
def move_turtle():
    x = random.randint(-280, 280)
    y = random.randint(-280, 280)
    t.goto(x, y)

# Fungsi untuk menangkap kura-kura
def catch_turtle(x, y):
    global score
    score += 1
    print("Kura-kura tertangkap! Skor:", score)
    move_turtle()

# Event untuk menangkap kura-kura
t.onclick(catch_turtle)

# Loop untuk gerakan kura-kura
def game_loop():
    move_turtle()
    wn.ontimer(game_loop, 2000)  # Pindah setiap 2 detik

# Mulai game
game_loop()

# Menjaga jendela tetap terbuka
wn.mainloop()
