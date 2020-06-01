>>> import turtle
>>> t = turtle.Pen()
>>> for x in range(100):
t.forward(x)
t.left(90)

>>> import turtle
>>> t = turtle.Turtle()
>>> t.pencolor('red')
>>> for x in range(100):
	t.circle(x)
	t.right(91)

>>> import turtle
>>> t = turtle.Pen()
>>> t.pencolor('purple')
>>> for x in range(100):
    t.backward(x)
    t.left(95)
	
import turtle
t = turtle.Pen()
colors = ['purple', 'green', 'red', 'blue']
for x in range(500):
    t.pencolor(colors[x%4])
    t.forward(x)
    t.right(95)

>>> import turtle
>>> t = turtle.Pen()
>>> colors = ['purple', 'pink', 'orange', 'green']
>>> turtle.bgcolor('black')
>>> for x in range(100):
	t.pencolor(colors[x%4])
	t.circle(x)
	t.left(95)    