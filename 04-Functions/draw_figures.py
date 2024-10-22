import turtle
import figures

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")
pen = turtle.Turtle()
pen.speed(5)
side_length = 100
side_length2 = 20
# figures.draw_square(side_length)
# figures.draw_triangle(side_length)
figures.draw_rectangle(side_length, side_length2)
window.mainloop()