#  Copyright (c) 2024 SGNetworks. All rights reserved.
#
#  The software is an exclusive copyright of "SGNetworks" and is provided as is exclusively with only "USAGE" access. "Modification",  "Alteration", "Re-distribution" is completely prohibited.
#  VIOLATING THE ABOVE TERMS IS A PUNISHABLE OFFENSE WHICH MAY LEAD TO LEGAL CONSEQUENCES.

def full_pyramid(rows = 5, char = "*"):
	for i in range(1, rows + 1):
		# Print leading spaces
		for j in range(rows - i):
			print(" ", end="")

		# Print asterisks for the current row
		for k in range(1, 2 * i):
			print(char, end="")
		print()

full_pyramid(5, "*")
