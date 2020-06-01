>>> def convert_in2cm(inches):
	return inches *2.54

>>> def convert_1b2kg(pounds):
	return pounds / 2.2
	>>> heightIn = int(input("Enter your height in inches:"))
#Enter your height in inches:65
>>> weight_1b = int(input("Enter your weight in pounds:"))
#Enter your weight in pounds:34
>>> height_cm = convert_in2cm(heightIn)
>>> weight_kg = convert_1b2kg(weight_1b)
>>> pingPongTall = round(height_cm/4)
>>> pingPongHeavy = round(weight_kg * 1000 / 2.7)
>>> feet = heightIn // 12
>>> inch = heightIn % 12
>>> print("At", feet, "feet", inch, "inches tall, and", weight_1b, "pounds",)
#At 5 feet 5 inches tall, and 34 pounds
>>> print("your measure", pingPongTall, "Ping-Pong balls tall, and")
#your measure 41 Ping-Pong balls tall, and
>>> print("you weigh the same as", pingPongHeavy, "Ping-Pong balls!")
#you weigh the same as 5724 Ping-Pong balls!

>>> import turtle
>>> t = turtle.Pen()
>>> t.speed(0)
>>> t.turtlesize(2,2,2)
>>> def up():
	t.forward(50)	
>>> def left():
	t.left(90)	
>>> def right():
	t.right(90)
>>> turtle.onkeypress(up, "Up")
>>> turtle.onkeypress(left, "Left")
>>> turtle.onkeypress(right, "Right")
>>> turtle.listen()
#program result = you get to use arrows to control where the turtle moves
