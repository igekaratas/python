# Guessing Game
# Guessing the numbers between 1 and 20

from random import randint


computer_number = randint(1,10)

guess_a_number = None

while guess_a_number != computer_number:
	guess_a_number = int(input("Guess a number between 1 and 10: "))
	if guess_a_number > computer_number:
		print("Try lower")
	elif guess_a_number < computer_number:
		print("Try higher")
	else:
		print("You got it!")
print(f"The number was: {computer_number}")





