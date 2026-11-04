# Created for: Introduction to Programming, Ariel University
# Exercise 3 - SOLUTIONS
# Topics: Strings, Approximation
#
# Every question is independent - run each block on its own.

############### Q1 ############
# Password checker 🔐
# The program gets a password from the user and checks that it is strong:
#   - at least 8 characters
#   - contains at least one digit
#   - contains at least one uppercase letter
# For every rule that is not met, print what is missing.
# If all the rules are met, print "Strong password 💪".
#
# Examples:
#   "hello"      ->  Too short (at least 8 characters)
#                    Missing a digit
#                    Missing an uppercase letter
#   "helloworld" ->  Missing a digit
#                    Missing an uppercase letter
#   "Hello2026"  ->  Strong password 💪
#
# Don't use string methods (like .isdigit() or .isupper()).
# Hint: use the strings below together with the operator "in".

digits = "0123456789"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

password = input("Enter a password: ")

has_digit = False
has_upper = False

for char in password:
    if char in digits:
        has_digit = True
    if char in uppercase:
        has_upper = True

if len(password) < 8:
    print("Too short (at least 8 characters)")
if not has_digit:
    print("Missing a digit")
if not has_upper:
    print("Missing an uppercase letter")

if len(password) >= 8 and has_digit and has_upper:
    print("Strong password 💪")


############### Q2 ############
# The Babylonian square root 🏛️
# About 3,500 years ago, the Babylonians found a fast way to approximate a square root:
#
#     new_guess = (guess + x / guess) / 2
#
# Why does it work? If guess is too BIG, then x / guess is too SMALL (and vice versa).
# The real root is somewhere between them - so we take their average.
#
# Write a program that gets a positive number x and approximates its square root:
#   - start with guess = x
#   - repeat the formula until |guess**2 - x| < epsilon   (epsilon = 0.0001)
#   - print every guess, and at the end the result and the number of guesses
#
# Example for x = 25:
#   guess 1: 13.0000
#   guess 2: 7.4615
#   guess 3: 5.4060
#   guess 4: 5.0152
#   guess 5: 5.0000
#   guess 6: 5.0000
#   5.0000 is close to the square root of 25.0 (6 guesses)
#   (guess 5 is 5.0000232... - it rounds to 5.0000 but is not yet within epsilon)

x = float(input("Enter a positive number: "))

epsilon = 0.0001
guess = x
num_guesses = 0

while abs(guess ** 2 - x) >= epsilon:
    guess = (guess + x / guess) / 2
    num_guesses += 1
    print(f"guess {num_guesses}: {guess:.4f}")

print(f"{guess:.4f} is close to the square root of {x} ({num_guesses} guesses)")
