#rock paper scissors

import random

def letter_to_number(letter):
	if letter == "rock":
		return 1
	if letter == "paper":
		return 2
	if letter == "scissors":
		return 3

def number_to_letter(num):
	if num == 1:
		return "rock"
	if num == 2:
		return "paper"
	if num == 3:
		return "scissors"

def rpc(guess):
	guessnum = letter_to_number(guess)
	rivalnum = random.randint(1,3)
	rival = number_to_letter(rivalnum)
	if (rivalnum - guessnum)%3 == 0:
		print guess + " and " + rival + " are equal"
	if (rivalnum - guessnum)%3 == 1:
		print guess + " beats " + rival 
	if (rivalnum - guessnum)%3 == 2:
		print guess + " was beaten by " + rival
	return

rpc("rock")
rpc("paper")
rpc("scissors")
