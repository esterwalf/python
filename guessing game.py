>>> import random
>>> theNumber = random.randint(1, 10)
>>> guess = int(input("Guess a number between 1 and 10: "))
#Guess a number between 1 and 10: 7
>>> while guess != theNumber:
	if guess > theNumber:
		print(guess, "was too high. try again.")
	if guess < theNumber:
		print(guess, "was too low. try againn.")
	guess = int(input("guess again:"))
#7 was too low. try againn.
#guess again:9
#9 was too low. try againn.
guess again:10
>>> print(guess, "was the number! you win!")
#10 was the number! you win!
>>> print(guess, "was the number! you win!")
#10 was the number! you win!

>>> colors = ["purple", "green", "blue", "orange", "yellow", "white"]
>>> random.choice(colors)
#'green'

>>> import random
>>> import turtle
>>> t = turtle.Pen()
>>> turtle.bgcolor("black")
>>> colors = ["yellow", "blue", "green", "pink", "white", "purple", "orange", "red"]
>>> for n in range(50): #generate random spirals of random sized/colors at random locations
	t.pencolor(random.choice(colors)) #pick a random color
	size = random.randint(10,40) #pick a random spiral size
	x = random.randrange(-turtle.window_width()//2,
			     turtle.window_width()//2) #generate a random x,y location on the screen
	y = random.randrange(-turtle.window_height()//2,
			     turtle.window_height()//2) #camel caps don't work on this code line
	t.penup()
	t.setpos(x,y)
	t.pendown()
	for m in range(size):
		t.forward(m*2)
		t.left(95)
		
>>> import random
>>> faces = ["ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king"]
>>> myFace = random.choice(faces)
>>> yourFace = random.choice(faces)
>>> if faces.index(myFace) > faces.index(yourFace):
	print("i win!")
elif faces.index(myFace) < faces.index(yourFace):
	print("you win!")