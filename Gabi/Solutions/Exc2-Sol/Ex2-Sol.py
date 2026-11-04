# Copyright © 2025 Lior Brown
# All rights reserved.
#
# Created for: Introduction to Programming, Ariel University

############### Q1 ############
# This program gets from the user 2 numbers and an operator: [+,-,/,*] and outputs the result

# Get the first number (assuming valid number input)
num1 = float(input("Enter the first number: "))

# Get the second number (assuming valid number input)
num2 = float(input("Enter the second number: "))

# Get the operator
operator = input("Enter the operator (+, -, *, /): ")

result = None  # Initialize result variable

# Use a while loop to ensure the operator is valid OR to prevent division by zero
invalid_operation = True
while invalid_operation:
    if operator == '+':
        result = num1 + num2
        invalid_operation = False
    elif operator == '-':
        result = num1 - num2
        invalid_operation = False
    elif operator == '*':
        result = num1 * num2
        invalid_operation = False
    elif operator == '/':
        # Check for division by zero
        if num2: # the same as if num2 != 0: (because if num2 is 0 it is False)
            result = num1 / num2
            invalid_operation = False
        else:
            print(
                "❌ Error: Division by zero is not allowed. Please re-enter a non-zero second number and the operator.")
            # Re-prompt for num2 and operator to re-enter the loop
            num2 = float(input("Enter the second number (must be non-zero): "))
            # Loop will continue with new values

    # Invalid operation
    else:
        print(f"❌ Error: Invalid operator '{operator}'. Please enter one of +, -, *, /.")
        # Re-prompt for the operator
        operator = input("Enter the operator (+, -, *, /): ")
        # Loop will continue with new value

# Display the result
print(f"\nResult: {num1} {operator} {num2} = {result:.2f}") # in an f string, :.2f formats to 2 decimal points, :.3f would do 3 decimals and so on

############### Q2 ############
# This program collects exam grades for a class and prints a summary 📊
# The program gets from the user:
#  1) The number of students (a positive integer)
#  2) A grade for each student (an integer between 0 and 100)
# Validation: If the input is out of range, the program prompts the user to enter it again
# Outputs: average, highest, lowest, passed/failed count (pass >= 60),
#          and a suggested factor if the average is below 70.
# No lists - everything is computed on the fly.

PASS_GRADE = 60
TARGET_AVERAGE = 70

# Get the number of students
num_students = int(input("Enter the number of students: "))
# We will make a while loop to continue asking untill input is positive
while num_students <= 0:
    num_students = int(input("Please insert a positive integer: "))

# Accumulators
total = 0
passed = 0
highest = -1   # Lower than any valid grade, so the first grade always replaces it
lowest = 101   # Higher than any valid grade, so the first grade always replaces it

# Loop over the students (k runs from 1 to num_students)
for k in range(1, num_students + 1):

    # Get and validate the grade
    grade = int(input(f"Enter the grade of student #{k}: "))
    # or you can write: grade = int(input("Enter the grade of student # " + k + ": "))

    # like we did before, if grade is not valid, we will continue to ask for Grade until it is valid
    while not 0 <= grade <= 100:
        grade = int(input("Please insert a valid grade (0-100): "))

    # Update the sum
    total += grade

    # Update highest / lowest
    if grade > highest:
        highest = grade
    if grade < lowest:
        lowest = grade

    # Count passing students
    if grade >= PASS_GRADE:
        passed += 1

failed = num_students - passed
average = total / num_students

# Display the summary
print("\n--- Class summary 📊 ---")
print(f"Average: {average:.2f}")
print(f"Highest: {highest} | Lowest: {lowest}")
print(f"Passed: {passed} ✅ | Failed: {failed} ❌")

# Suggest a factor if needed
if average < TARGET_AVERAGE:
    factor = TARGET_AVERAGE - average
    print(f"Suggested factor: {factor:.2f} points 🎁")
else:
    print("No factor needed 🎉")