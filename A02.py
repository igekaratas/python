#
# Name: Mehmet Karatas
# SSID: 1640957
# Assignment #: 2
# Submission Date: 9/11/18
# Description of program:
# This is a trivia quiz about Santa Monica College
#

j = 0 # Creating loop with while loops.
while j < 1:
	print("\n**************************************************\n")
	print("Welcome to the History Quiz.\n")
	print("Win by answering all three questions correctly.\n")
	print("**************************************************\n")
	# I choose 3 questions for users.
	print("1. Who was the first president of the USA?	\n")
	print("a. George Washington")
	print("b. George W Bush")
	print("c. John F Kennedy")
	print("d. Abraham Lincoln\n")

	userInput1 = input("Enter your answer (a,b,c, or d): ")

	if userInput1 == "a":
		print("Well Done! Answer the next \n")
	else:
		print("Nope! Try next question\n")

	print("2. Who was the first Western explorer to reach China?\n")
	print("a. Magellan")
	print("b. Cook")
	print("c. Marco Polo")
	print("d. Amerigo Vespucci")

	userInput2 = input("Enter your answer (a,b,c, or d): ")

	if userInput2 == "c":
		print("You are really smart! Answer the next question\n")
	else:
		print("That is wrong! Lets try another question.\n")

	print("What is USA's national bird?")
	print("a. Woodpecker")
	print("b. Bald Eagle")
	print("c. Hummingbird")
	print("d. Sparrow")

	userInput3 = input("Enter your answer (a,b,c, or d): ")

	if userInput3 == 'b':
		print("You are right!\n")
	else:
		print("Better luck next time\n")
	# If user answer all correctly finish the quiz.
	if userInput1 == 'a' and userInput2 == 'c' and userInput3 == 'b':
		print("You answered all questions correctly.")
		print("Thanks for playing.\n")
		break
	else:
		# While user did not answer all questions correctly
		# we are asking them if they want to play again.
		askIfPlayAgain = input("Do you want to play again? (y) or (n): ")
		if askIfPlayAgain == 'y':
			print("OK, Here we go again!!\n")
		else:
			print("THANKS FOR PLAYING\n")
			break




	




