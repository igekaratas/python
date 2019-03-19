#
# Name: Mehmet Karatas
# SSID: 1640957
# Assignment #: 4
# Submission Date: 10/16/18 
# Description of program:
# The fourth assignment will use Python lists and the 
# def keyword to create functions that work on a 2D matrix. 
# All three functions will return a result.
# In linear algebra we learn how to work on an arrangement of numbers 
# called a matrix that is assembled into rows and columns. 
# A matrix can be created in Python as a list of lists, also 
# called a two-dimensional table. There are many operations on 
# matrices but we will just code three of them in Python.
# 

# # This problem is for testing purposes
# m1 = [
# 	[1,2,3,4],
# 	[5,6,7,8],
# 	[9,10,11,12],
# 	[13,14,15,16,]
# 	]

# # Symmetric Matrix. For testing.
# m3 = [
# 	[1,7,3],
# 	[7,4,5],
# 	[3,5,6]
# 	]


def diagonal(x):
    diag = []
    for i in range(0, len(x)):
        diag.append(x[i][i]) 
    return diag


def symmetric(x):
	for i in range(len(x)):
		for j in range(len(x)):
			if(x[i][j] != x[j][i]):
				return False
	return True

def transpose(x):
	trns = []
	for i in range(len(x)):
		trns_row = []
		for row in x:
			trns_row.append(row[i])
		trns.append(trns_row)
	return trns

# This print function is for testing purpose.
# print(diagonal(m3))








