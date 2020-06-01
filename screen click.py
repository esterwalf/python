>>> import random
>>> import turtle
>>> t = turtle.Pen()
>>> t.speed(0)
>>> turtle.bgcolor("Black")
>>> colors = ["purple", "orange", "white", "green", "blue", "red", "yellow", "pink"]
>>> def spiral (x,y):
	t.pencolor(random.choice(colors))
	size = random.randint(10,40)
	t.penup()
	t.setpos(x,y)
	t.pendown()
	for m in range(size):
		t.forward(m*2)
		t.left(95)		
>>> turtle.onscreenclick(spiral)

>>> import random
>>> import turtle
>>> t = turtle.Pen()
>>> turtle.bgcolor("black")
>>> t.hideturtle()
>>> t.speed(0)
>>> colors = ["purple", "orange", "white", "green", "blue", "red", "yellow", "pink"]
>>> def drawKaleido(x,y):
	t.pencolor(random.choice(colors))
	size = random.randint(10,40)
	drawSpiral(x,y, size)
	drawSpiral(-x,y, size)
	drawSpiral(-x,-y, size)
	drawSpiral(x,-y, size)
>>> def drawSpiral(x,y, size):
	t.penup()
	t.setpos(x,y)
	t.pendown()
	for m in range(size):
		t.forward(m*2)
		t.left(95)		
>>> turtle.onscreenclick(drawKaleido)