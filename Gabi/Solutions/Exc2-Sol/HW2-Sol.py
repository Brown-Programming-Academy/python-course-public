# Copyright © 2026 Lior Brown
# All rights reserved.
#
# Created for: Introduction to Programming, Ariel University

############### Q1 ############
# Guess the number 🎯
# The secret number is YOUR year of birth 🎂 (define it as a constant at the top of the program)
# The user has 7 attempts to guess a year between 1900 and 2026
# After each guess the program prints: "Too high!" 📉 or "Too low!" 📈
# Correct guess - print in which attempt the user succeeded
# Out of attempts - reveal the secret number
# Validation: A guess out of range (1900-2026) - print an error and ask again, WITHOUT losing an attempt

# The secret number - replace with your year of birth
SECRET_YEAR = 1987

is_guessed = False

# Each iteration is one attempt
for attempt in range(1, 8):
    guess = int(input(f"Attempt {attempt}/7: "))

    # Re-prompt until the guess is in range - the attempt is not lost
    while not 1900 <= guess <= 2026:
        print("❌ Year must be between 1900 and 2026.")
        guess = int(input(f"Attempt {attempt}/7: "))

    if guess > SECRET_YEAR:
        print("📉 Too high!")
    elif guess < SECRET_YEAR:
        print("📈 Too low!")
    else:
        print(f"🎉 Correct! You got it in {attempt} attempts.")
        is_guessed = True
        break

# The loop ended without a correct guess
if not is_guessed:
    print(f"😢 Out of attempts. The year was {SECRET_YEAR}.")

############### Q2 ############
# ATM 🏧
# The PIN is YOUR year of birth 🎂 and the starting balance is 1000
# The user has 3 attempts to enter the PIN. 3 mistakes - the card is blocked 🔒 and the program ends
# After a correct PIN, a menu is shown again and again until the user chooses to exit:
#  1) Balance 💰
#  2) Deposit 📥
#  3) Withdraw 📤
#  4) Exit 👋
# Validation:
#  - Invalid choice (not 1-4) - print an error and go back to the menu
#  - Withdraw - a positive amount, in multiples of 50, and not more than the balance. Otherwise - print an error

# The PIN - replace with your year of birth
PIN = 1987

balance = 1000
is_logged_in = False

# Up to 3 attempts to enter the PIN
for attempt in range(1, 4):
    pin = int(input("Enter PIN: "))

    if pin == PIN:
        print("✓ Welcome!")
        is_logged_in = True
        break

    if attempt < 3:
        print(f"❌ Wrong PIN. {3 - attempt} attempts left.")
    else:
        print("❌ Wrong PIN.")

if not is_logged_in:
    print("🔒 Card blocked.")
else:
    print("1) Balance 💰  2) Deposit 📥  3) Withdraw 📤  4) Exit 👋")
    choice = 0

    # Show the menu until the user chooses to exit
    while choice != 4:
        choice = int(input("Choice (1-4): "))

        # Balance
        if choice == 1:
            print(f"Balance: {balance}")

        # Deposit
        elif choice == 2:
            amount = int(input("Amount: "))

            if amount <= 0:
                print("❌ Amount must be positive.")
            else:
                balance += amount
                print(f"Deposited {amount}. Balance: {balance}")

        # Withdraw
        elif choice == 3:
            amount = int(input("Amount: "))

            if amount <= 0:
                print("❌ Amount must be positive.")
            elif amount % 50 != 0:
                print("❌ Amount must be a multiple of 50.")
            elif amount > balance:
                print(f"❌ Insufficient funds (balance: {balance}).")
            else:
                balance -= amount
                print(f"Withdrew {amount}. Balance: {balance}")

        # Exit
        elif choice == 4:
            print("Goodbye 👋")

        # Invalid choice
        else:
            print("❌ Invalid choice. Please choose 1-4.")

############### Q3 ############
# Perfect numbers 🌟
# A perfect number is a number that equals the sum of its divisors (not including itself)
# For example: 6 = 1 + 2 + 3
# The program gets an integer N and prints all the perfect numbers up to N - each one with its divisors
# At the end, the program prints how many perfect numbers were found
# Validation: N must be greater than 1 - otherwise print an error and ask again

n = int(input("Enter N: "))

while n <= 1:
    print("❌ N must be greater than 1.")
    n = int(input("Enter N: "))

count = 0

for num in range(2, n + 1):

    # Sum the divisors of num (a divisor is never bigger than num // 2)
    divisors_sum = 0
    for divisor in range(1, num // 2 + 1):
        if num % divisor == 0:
            divisors_sum += divisor

    if divisors_sum == num:
        count += 1

        # 1 is always a divisor, so print it first and add " + divisor" for the rest
        print(num, "= 1", end="")
        for divisor in range(2, num // 2 + 1):
            if num % divisor == 0:
                print(" +", divisor, end="")

        # Close the line
        print()

print(f"Found {count} perfect numbers 🌟")

############### Q4 ############
# Collatz conjecture 🪜
# Start from a positive number and repeat the rule until reaching 1:
#  - Even:  n // 2
#  - Odd:   3 * n + 1
# For example: 6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1 (8 steps)
# The program gets an integer N, prints for each number from 1 to N how many steps it took to reach 1,
# and at the end announces the champion - the number with the most steps 🏆
# Validation: N must be positive - otherwise print an error and ask again

n = int(input("Enter N: "))

while n <= 0:
    print("❌ N must be positive.")
    n = int(input("Enter N: "))

champion = 1
max_steps = 0

for num in range(1, n + 1):

    # Walk the Collatz path of num until reaching 1
    current = num
    steps = 0
    while current != 1:
        if current % 2 == 0:
            current //= 2
        else:
            current = 3 * current + 1
        steps += 1

    print(f"{num} → {steps} steps")

    # Keep the number with the most steps so far
    if steps > max_steps:
        max_steps = steps
        champion = num

print(f"🏆 Champion: {champion} with {max_steps} steps")
