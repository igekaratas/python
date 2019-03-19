# Rock Scissors Paper with while loop.

from random import randint

computer_wins = 0
player_wins = 0
winning_score = 3

while computer_wins < winning_score and player_wins < winning_score:
	print("\n~ Rock ~ Scissors ~ Paper ~ ")

	user_input = input("Choose your selection: ").lower()
	if user_input == "quit" or user_input == "q":
		break

	random_number = randint(1,2)

	if random_number == 0:
		computer = "rock"
	elif random_number == 1:
		computer = "paper"
	else:
		computer = "scissors"

	print(f"The computer plays: {computer}")

	if user_input == computer:
		print("It is a tie.")
	elif user_input == "rock":
		if computer == "paper":
			print("Computer wins :(")
			computer_wins += 1
		else:
			print("You won.")
			player_wins += 1
	elif user_input == "paper":
		if computer == "rock":
			print("You won :(")
			player_wins += 1
		else:
			print("Computer won.")
			computer_wins += 1
	elif user_input == "scissors":
		if computer == "rock":
			print("Computer won :(")
			computer_wins += 1
		else: 
			print("You won!")
			player_wins += 1
	else:
		print("Please only input \"rock\", \"scissors\" or  \"paper\" ")
	print(f"\nComputer Score: {computer_wins} Player Score: {player_wins}")

if player_wins > computer_wins:
	print("Congrats! You won")
elif player_wins == computer_wins:
	print("IT IS A TIE!!")
else:
	print("Try again later.")







