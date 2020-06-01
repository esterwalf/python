>>> import turtle #set up turtle graphics
>>> t = turtle.Pen()
>>> turtle.bgcolor("black")
>>> colors = ["green", "purple", "orange", "white", "yellow", "pink", "blue", "red"]
>>> family = [] #set up an empty list for family names
>>> name = turtle.textinput("My family",
			"Enter a name, or just hit [ENTER] to end:") #ask for their first name
>>> while name != "": #keep asking for names
	family.append(name) #add their name to the family list
	name = turtle.textinput("My family",
				"Enter a name, or just hit [ENTER] to end:") #ask for another name or end
>>> for x in range(100): #draw a spiral of the names on the screen
		t.pencolor(colors[x%len(family)]) #rotate through the colors
		t.penup() #dont draw regular spiral lines
		t.forward(x*4) #just move the turtle on the screen
		t.pendown() #draw the next family member's name
		t.write(family[x%len(family)], font = ("Arial", int((x+4)/4), "bold") ) 
		t.left(360/len(family + 2)) #turn left for our spiral len=length
		
>>> import turtle
>>> t = turtle.Pen()
>>> turtle.bgcolor("black")
>>> sides = int(turtle.numinput("Number of sides", "How many sides in your spirals (2-4)?", 4, 2, 6))
>>> colors = ["red", "yellow", "blue", "green", "purple", "orange"]
>>> for m in range(100):
	t.forward(m*4)
	position = t.position() #remember this corner of the spiral
	heading = t.heading() #remember the direction we're heading
>>> for n in range(int(m/2)):
	t.penup()
	t.pencolor(colors[m%sides])
	t.forward(2*n)
	t.right(360/sides - 2)
	t.pendown()
>>> t.setx(position[0]) #go back to the big spiral's x location
>>> t.sety(position[1]) #go back to the big spiral's y location
>>> t.setheading(heading) #point in the big spiral's heading
>>> t.left(360/sides + 2) #aim at the next point on the big spiral