#!/usr/bin/python3

import random
number = random.randint(-10000, 10000)

if number < 0:
	lastnumber = ((number *-1) % 10) * -1
else:
	lastnumber = number % 10
	if (lastnumber == 0):
		print("Last digit of {} is {} and is 0".format(number, lastnumber))
	elif lastnumber > 5:
		print("Last igit of {} is {}".format(number, lastnumber), end=" ")
	else: 
		print("Last digit of {} is {}".format(number, lastnumber), end=" ")
		print("and is less than 6 and not 0")
