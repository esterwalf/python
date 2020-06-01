>>> message = input("Enter a message to encode or decode")
#Enter a message to encode or decode answer me
>>> message = message.upper()
>>> output = "" #create an empty string to hold output
>>> for letter in message: #loop through each letter of the message
	if letter.isupper(): #if the letter is in the alphabet (A-Z)
		value = ord(letter)+13 #shift the letter value up by 13
		letter = chr(value) #turn the value back into a letter
		if not letter.isupper(): #check to see if we shifted too far
			value -= 26 #if we did wrap it back around Z->A
			letter = chr(value) #by subtracting 26 from the letter value
	output += letter #add the letter to our output string
>>> print("Output message: ", output) #output the encoded/decoded message
#Output message:   NAFJRE ZR

>>> import random
>>> suits = ["clubs", "spades", "hearts", "diamonds"]
>>> faces = ["ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king"]
>>> keepGoing = True
>>> while keepGoing:
	myFace = random.choice(faces)
	mySuit = random.choice(suits)
	yourFace = random.choice(faces)
	yourSuit = random.choice(suits)
	print("I have the", myFace, "of", mySuit)
	print("you have the", yourFace, "of", yourSuit)
	if faces.index(myFace) > faces.index(yourFace):
		print("I win!")
	elif faces.index(myFace) < faces.index(yourFace):
		print("you win!")
	else:
		print("it's a tie!")
	answer = input("hit [ENTER] to keep going, any key to exit:")
	keepGoing = (answer == "")

