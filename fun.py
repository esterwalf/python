>>> answer = input("Do you want to see a spiral? y/n:").lower()
#Do you want to see a spiral? y/n:y
>>> if answer == "y" or == "yes":
	print("working...")
	import turtle
	t = turtle.Pen()
	t.width(2)
	for x in range(100):
		t.forward(x*2)
		t.left(85)		
working...
>>> print("okay, we're done!")
#okay, we're done!

>>> drivingAge = eval(input("What is the legal driving age where you live?"))
#What is the legal driving age where you live? 18
>>> yourAge = eval(input("How old are you?"))
#How old are you? 25
>>> if yourAge >= drivingAge:
	print("You're old enough to drive!")
>>> else: 
	print("sorry you can drive in", drivingAge - yourAge, "years.")