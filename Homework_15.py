import tkinter as tk
from random import randint
import turtle

def roll_die():
    result = randint(1, 6)
    result_label.config(text=str(result))
    draw_cube(result)

def draw_cube(number):
    cube = turtle.Turtle()
    cube.speed(2)
    cube.penup()
    cube.goto(-50, -50)
    cube.pendown()
    cube.begin_fill()

    for _ in range(4):
        cube.forward(120)
        cube.left(90)

    cube.end_fill()
    cube.penup()
    cube.goto(10, 0)
    cube.pendown()
    cube.color("pink")
    cube.write(number, align="center", font=("Arial", 40, "bold"))
    cube.hideturtle()

window = tk.Tk()
window.title("Die Roller")

roll_button = tk.Button(window, text="Roll Die", command=roll_die)
roll_button.pack(pady=10)

result_label = tk.Label(window, text="", font=("Helvetica", 24))
result_label.pack()

turtle_canvas = tk.Canvas(window, width=600, height=600)
turtle_canvas.pack()

window.mainloop()
