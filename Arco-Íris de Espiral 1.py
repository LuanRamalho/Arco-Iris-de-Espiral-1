import  turtle
from turtle import  *

a = turtle.Screen()
turtle.title('Arco Íris de Espiral')
turtle.speed(0)
turtle.bgcolor('black')
r,g,b = 255, 0, 0

for i in range(255*2):
    colormode(255)
    if (i<255//3):
        g = g + 3
    elif (i<255*2//3):
        r = r - 3
    elif (i<255):
        b = b + 3
    elif (i<255*4//3):
        g = g - 3
    elif (i<255*5//3):
        r = r + 3
    else:
        b = b - 3

    turtle.fd(50+i)
    turtle.rt(91)
    turtle.pencolor(r,g,b)
a.exitonclick()