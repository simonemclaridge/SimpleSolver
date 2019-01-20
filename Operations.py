# #############################################
# File name: Operations.py                    #
# Author: Simone Claridge                     #
# Date created: 12/20/2018                    #
# Python Version: 3.7.2                       #
#                                             #
# Test class for GUI solve functions          #
###############################################

# asks user for first operand, accepts input
first_operand = input("Enter an operand: ")

# asks user for operand, accepts input
operator = input("Enter an operator: ")

# asks user for second operand, accepts input
second_operand = input("Enter the second operand:  ")


# solves numeric operations
def solveMath(first_operand, operator, second_operand):
	if first_operand.isdecimal() & second_operand.isdecimal():
		if operator == '+':
			result = int(first_operand) + int(second_operand)
			print(result)
		if operator == "-":
			result = int(first_operand) - int(second_operand)
			print(result)
		if operator == "*":
			result = int(first_operand) * int(second_operand)
			print(result)
		if operator == "/":
			result = int(first_operand) / int(second_operand)
			print(result)
	else:
		print("Can not perform operation")


# solves relational operations
def solveRelational(first_operand, operator, second_operand):
	if first_operand.isdecimal() & second_operand.isdecimal():
		if operator == '>':
			if first_operand > second_operand:
				result = True
				print(result)
			else:
				result = False
				print(result)
		if operator == "<":
			if first_operand < second_operand:
				result = True
				print(result)
			else:
				result = False
				print(result)
		if operator == "=":
			if first_operand == second_operand:
				result = True
				print(result)
			else:
				result = False
				print(result)
	else:
		print("Can not perform operation")


solveMath(first_operand, operator, second_operand)
solveRelational(first_operand, operator, second_operand)
