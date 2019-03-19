#
# Name: Mehmet Karatas
# SSID: 1640957
# Assignment #: 3
# Submission Date: 
# Description of program:
# Convert upper case to lower case and lower case to upper case
#

user_input_sentence = input("Enter sentence to convert opposite cases: ")


for i in user_input_sentence:
	if i.isupper():
		make_lower = user_input_sentence.lower()
		print(make_lower)
	else:
		make_upper = user_input_sentence.upper()
		print(make_upper)

# 
# ### I tried a few things but I couldnt make it, I will finish later. ##
# 

# uInput = input("Enter the ")

# j = 1
# while j < 0:
# 	convert_to_upper = uInput.upper()
# 	print(convert_to_upper)
# 	if uInput == 'q':
# 		print("Goodbye")
# 		break
# 	else:
# 		uInput = input("Enter the ")

	

