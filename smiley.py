>>> import random
>>> import turtle
>>> t = turtle.Pen()
>>> t.speed(0)
>>> t.hideturtle()
>>> turtle.bgcolor("black")
>>> def drawSmiley(x,y):
	t.penup()
	t.setpos(x,y)
	t.pendown()
	#head
	t.pencolor("yellow")
	t.fillcolor("yellow")
	t.begin_fill()#don't use camel caps
	t.circle(50)
	t.end_fill()#camel cups don't work
	#left eye
	t.setpos(x-15, y+60)
	t.fillcolor("blue")
	t.begin_fill()#don't use camel caps
	t.circle(10)
	t.end_fill()#camel cups don't work
	#right eye
	t.setpos(x+15, y+60)
	t.begin_fill()#don't use camel caps
	t.circle(10)
	t.end_fill() #camel cups don't work
	#mouth
	t.setpos(x-25, y+40)
	t.pencolor("black")
	t.width(10)
	t.goto(x-10, y+20)
	t.goto(x+10, y+20)
	t.goto(x+25, y+40)
	t.width(1)
>>> for n in range(50):
	x = random.randrange(-turtle.window_width()//2,
			     turtle.window_width()//2) #camel caps dont work in these brackets
	y = random.randrange(-turtle.window_height()//2,
			     turtle.window_height()//2)#camel caps dont work in these brackets
>>> turtle.onscreenclick(drawSmiley)

