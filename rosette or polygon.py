>>> import turtle
>>> t = turtle.Pen()
>>> number = int(turtle.numinput("Number of sides or circles",
			     "How many sides or circles in your shape?", 6))
>>> shape = turtle.textinput("which shape do you want?",
			 "Enter 'p' for polygon or 'r' for rosette:")
>>> for x in range(number):
	if shape == 'r':
		t.circle(100)
		t.left(95)
	else:
		t.forward (150)
		t.left(360/number)
		
>>> import turtle
>>> t = turtle.Pen()
>>> sides = int(turtle.numinput("Number of sides",
			    "How many sides in your spiral?"))
>>> for m in range(5,75): #our outer spiral loop for polygons and rosettes, from size 5-75
	t.left(360/sides + 5)
	t.width(m//25+1)
	t.penup() #don't draw lines on spiral
	t.forward(m*4) #move to next corner
	t.pendown() #get ready to draw
	if (m % 2 == 0):
		for n in range(sides):
			t.circle(m/3)
			t.right(360/sides)
	else: #or, draw a little polygon at each ODD corner of the spiral
    	for m in range(sides):
			t.forward(m)
			t.right(360/sides)