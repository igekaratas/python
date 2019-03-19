# Guessing game 2nd version
# Asking user if they want to keep playing.

from random import randint


computer_number = randint(1,10) # Generating number between 1 - 10

while True:
	# Asking user for input and converting to integer.
	guess_a_number = int(input("Guess a number between 1 and 10: "))
	if guess_a_number > computer_number:
		print("Try lower")
	elif guess_a_number < computer_number:
		print("Try higher")
	else:
		print(f"You got it! \nThe number was: {computer_number}")
		play_again = input("Do you want to play again? (y/n): ")
		if play_again == "y":
			computer_number = randint(1,10) 
			guess_a_number = None
		else:
			print("Thanks for playing. Have a good one.")
			break


