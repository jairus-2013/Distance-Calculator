#DISTANCE FORMULA

import math


#Asks the user for the inputs needed for the code

var_x1 = float(input("Enter your first x-value: "))
var_x2 = float(input("Enter your second x-value: "))
var_y1 = float(input("Enter your first y-value: "))
var_y2 = float(input("Enter your second y-value: "))

#Formula for the given inputs are found below:

distance = math.sqrt(math.pow((var_x2 - var_x1), 2) + math.pow((var_y2 - var_y1), 2))
print(f"The distance between the two points is {distance}")

#The library helped me by making coding more efficient. Without it, I would have to make my own library from scratch.
