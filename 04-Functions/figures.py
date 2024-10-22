import turtle

def draw_square(lenght, pen):
    pen.speed(5)
    for i in range(4):
        pen.forward(lenght)
        pen.right(90)

def draw_triangle(length, pen):
    pen.speed(5)
    for i in range(3):
        pen.forward(length)
        pen.right(120)

def draw_rectangle(lenght_a, lenght_b, pen):
    pen.speed(5)
    for i in range(2):
        pen.forward(lenght_a)
        pen.right(90)
        pen.forward(lenght_b)
        pen.right(90)

