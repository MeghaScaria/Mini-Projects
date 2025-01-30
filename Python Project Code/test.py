import turtle
turtle.bgcolor("lightpink")
turtle.pensize(2.5)
turtle.speed(0.00001)
color = ["pink","lavender","purple","violet"]
for a in range (100):
    for i in color:
        turtle.color(i)
        turtle.circle(100)
        turtle.left(5)


turtle.mainloop()