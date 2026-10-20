# Copyright © 2025 Lior Brown
# All rights reserved.
#
# Created for: Introduction to Programming, Ariel University

############### Q1 ############
# This program asks for the user's name
# and greets them with a personalized good-morning message.

name = input("Please insert your name: ") # קלט
message = f"Good morning {name} you are champion" # עיבוד
print(message) # פלט

############### Q2 ############
# This program asks for the circle's radius and outputs its area and circumference.

############### Q3 ############
# This program gets an integer from the user and outputs 1 if it's even, and 0 if it's odd.

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
