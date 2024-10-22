###
# Draws each of the figures (square, triangle, rectangle) twice,
# in different locations
#
import figures
import turtle

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)   
side_length = 100
side_length2 = 20
## Draw figures
pen.penup()
pen.goto(0,0)
pen.pendown()
figures.draw_square(side_length, pen)

pen.penup()
pen.goto(-100,-100)
pen.pendown()
figures.draw_square(side_length, pen)

pen.penup()
pen.goto(200,200)
pen.pendown()
figures.draw_triangle(side_length, pen)

pen.penup()
pen.goto(0,-200)
pen.pendown()
figures.draw_triangle(side_length, pen)

pen.penup()
pen.goto(-200,100)
pen.pendown()
figures.draw_rectangle(side_length,side_length2, pen)

pen.penup()
pen.goto(100,150)
pen.pendown()
figures.draw_rectangle(side_length,side_length2, pen)



# Hide the turtle and finish
pen.hideturtle()
window.mainloop()