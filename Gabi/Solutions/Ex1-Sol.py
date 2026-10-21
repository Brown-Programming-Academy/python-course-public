# Copyright © 2025 Lior Brown
# All rights reserved.
#
# Created for: Introduction to Programming, Ariel University

############### Q1 ############
# This program asks for the user's name
# and greets them with a personalized good-morning message.

name = input("Please insert your name:")
# option 1: print ("Good morning Mr", name, ",how do you feel today? 🤗")
# option 2 (best practice✔️):
print(f"Good morning Mr {name} ,how do you feel today? 🤗")
# option 3: print (f"Good morning Mr {input("Please insert your name:")} ,how do you feel today? 🤗")

############### Q2 ############
# This program asks for the circle's radius and outputs its area and circumference.

import math  # Import the math module to use the constant π (pi)

# Ask the user to enter the radius of the circle
radius = float(input("Please enter the circle's radius: "))

# Calculate the area using the formula: π * r²
area = math.pi * radius ** 2

# Calculate the circumference using the formula: 2 * π * r
circumference = 2 * math.pi * radius

# Display the results, rounded to 2 decimal places
print(f"The area is {area:.2f}")
print(f"The circumference is {circumference:.2f}")

############### Q3 ############
# This program gets an integer from the user and outputs 1 if it's even, and 0 if it's odd.

# Ask the user for a number (convert the input text to an integer)
n = int(input("Enter an integer: "))

# Calculate 1 if even and 0 if odd, using pure mathematics
# n % 2 gives 0 for even and 1 for odd → we flip it with (1 - ...)
result = 1 - n % 2

# Display the result to the user
print(result)

############### Q4 ############
# This program gets three integers from the user:
# 1) The number of holes in the piccolo.
# 2) The jump length (how many holes the finger moves each time).
# 3) The number of jumps.
#
# The finger starts on the first hole (hole 1, not 0).
# It moves forward by the given jump length, one jump at a time.
# When it passes the last hole, it wraps around to the beginning.
# The program outputs the hole number where the finger ends up.
#
# Example:
# If there are 6 holes, the jump length is 2, and the number of jumps is 4:
# Start → 1
# 1st jump → 3
# 2nd jump → 5
# 3rd jump → 1 (wraps around)
# 4th jump → 3
# Result → 3

# Get input values from the user
holes = int(input("Enter the number of holes: "))
jump = int(input("Enter the jump length: "))
jumps = int(input("Enter the number of jumps: "))

# Calculate the final hole number (1-based)
result = (jump * jumps) % holes + 1

# Display the result
print(f"The finger ends on hole number {result}")
