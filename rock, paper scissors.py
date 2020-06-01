>>> import random
>>> choices = ["rock", "paper", "scissors"]
>>> print("rock crushes scissors, scissors crush paper, paper crushes rock")
rock crushes scissors, scissors crush paper, paper crushes rock
>>> player = input("do you want to be rock, paper or scissors (or quit)")
do you want to be rock, paper or scissors (or quit)rock
>>> while player != "quit":
	player = player.lower()
	computer = random.choice(choices)
	print("you chose" +player+ ", and the computer chose" +computer+ ".")
	if player == computer:
		print("it's a tie!")
	elif player == "rock":
		if computer == "scissors":
			print("you win!")
		else:
			print("computer wins")
	elif player == "scissors":
		if computer == "paper":
			print("you win!")
		else:
			print("computer wins")
	elif player == "paper":
		if computer == "rock":
			print("you win!")
		else:
			print("computer wins")
	else:
		print("um... i think there was some sort of error")
	print()
	player = input("do you want to be rock paper scissors (or quit)?")