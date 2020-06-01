>>> import turtle
>>> t = turtle.Pen()
>>> t.circle(100)
>>> t.left(90)
>>> t.circle(100)
>>> t.left(90)
>>> t.circle(100)
>>> t.left(90)
>>> t.circle(100)

>>> import turtle
>>> t = turtle.Pen()
>>> for x in range(4):
	t.circle(100)
	t.left(90)

>>> import turtle
>>> t = turtle.Pen()
>>> numberOfCircles = int(turtle.numinput("number of circles",
				      "how many circles in your rosette?", 6))
>>> for x in range(numberOfCircles):
	t.circle(100)
	t.left(360/numberOfCircles)
	
name = input("what is your name?")
>>> while name != "":
	for x in range(100):
		print(name, end = " ")
		print()
		name = input("type another name, or just hit [ENTER] to quit: ")
		print("Thanks for playing!")

