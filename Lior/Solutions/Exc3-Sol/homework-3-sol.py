# Created for: Introduction to Programming, Ariel University
# Homework 3 (optional) - SOLUTIONS
# Topics: Guess-and-Check, Strings, Loops
#
# The questions are ordered from easier to harder.
# Every question is independent - run each block on its own.

############### Q1 ############
# Chickens and cows 🐔🐄
# A farmer has only chickens and cows.
# Every chicken has 1 head and 2 legs, every cow has 1 head and 4 legs.
#
# The program gets the total number of heads and the total number of legs,
# and finds how many chickens and how many cows there are.
# If there is no valid answer, print "No solution".
#
# Examples:
#   heads = 10, legs = 32  ->  4 chickens and 6 cows
#   heads = 10, legs = 31  ->  No solution
#   heads = 3,  legs = 6   ->  3 chickens and 0 cows
#
# Use guess-and-check: guess every possible number of chickens (from 0 up to heads),
# the rest of the heads must be cows - then check if the legs add up.

heads = int(input("Enter the number of heads: "))
legs = int(input("Enter the number of legs: "))

found = False
for chickens in range(heads + 1):        # guess: 0, 1, 2, ..., heads chickens
    cows = heads - chickens               # the rest are cows
    if 2 * chickens + 4 * cows == legs:   # check
        print(f"{chickens} chickens and {cows} cows")
        found = True
        break

if not found:
    print("No solution")


############### Q2 ############
# Is it prime? 🔢
# Background:
#   A prime number is an integer greater than 1 that divides ONLY by 1 and by itself.
#   Prime numbers: 2, 3, 5, 7, 11, 13, 17, ...
#   Not prime:     4 (= 2 * 2), 9 (= 3 * 3), 12 (= 2 * 6), ...
#   Notes: 1 is NOT prime (by definition). 2 is the only even prime.
#
# The program gets a positive integer n and checks whether it is prime.
#   - If it is prime, print "<n> is prime".
#   - If it is not, print "<n> is not prime" and its SMALLEST divisor (other than 1).
#   - For n = 1 print "1 is not prime".
#
# Examples:
#   7   ->  7 is prime
#   12  ->  12 is not prime (divisible by 2)
#   91  ->  91 is not prime (divisible by 7)
#   97  ->  97 is prime
#   1   ->  1 is not prime
#
# Use guess-and-check: guess every possible divisor d from 2 up to n - 1,
# and check whether n % d == 0. As soon as you find one - you can stop.
#
# Questions for thought:
#   a) For n = 97, how many divisors did your program check?
#   b) Why is it enough to check only divisors d where d * d <= n ?
#   c) Bonus: change your program to check only d * d <= n (use a while loop).
#      How many divisors does it check now for n = 97?
#
# Answers:
#   a) 95 divisors (2, 3, ..., 96).
#   b) If n is not prime, then n = a * b with 2 <= a <= b.
#      Then a * a <= a * b = n. So if n has a divisor at all, it has one with d * d <= n.
#      If we found nothing up to there - there is nothing to find. 
#   c) Only 8 divisors (2, 3, ..., 9), because 10 * 10 = 100 > 97.
#      For bigger numbers the difference is huge: for 1,000,003 it's ~1,000 checks
#      instead of ~1,000,000. See the bonus code below.

n = int(input("Enter a positive integer: "))

if n < 2:
    print(f"{n} is not prime")
else:
    is_prime = True
    for d in range(2, n):            # guess every possible divisor
        if n % d == 0:               # check
            print(f"{n} is not prime (divisible by {d})")
            is_prime = False
            break                    # found one - no need to continue
    if is_prime:
        print(f"{n} is prime")

# ---- Bonus (c): check only d * d <= n ----
n = int(input("Enter a positive integer: "))

if n < 2:
    print(f"{n} is not prime")
else:
    is_prime = True
    d = 2
    while d * d <= n:
        if n % d == 0:
            print(f"{n} is not prime (divisible by {d})")
            is_prime = False
            break
        d += 1
    if is_prime:
        print(f"{n} is prime")


############### Q3 ############
# Find the word 🔍
# The program gets a sentence and a word, and prints the index where the word
# FIRST appears in the sentence. If it does not appear, print "Not found".
#
# You may NOT use "in" on the sentence, or string methods like .find()
# Use guess-and-check: guess every possible starting position i,
# and check if the slice of the sentence that starts at i is equal to the word.
#
# Examples:
#   sentence = "the cat sat on the mat", word = "the"  ->  Found at index 0
#   sentence = "the cat sat on the mat", word = "mat"  ->  Found at index 19
#   sentence = "the cat sat on the mat", word = "dog"  ->  Not found
#
# Hint: the slice sentence[i:i + len(word)] has the same length as the word.
#
# Questions for thought:
#   a) What is the LAST starting position worth checking? Why?
#   b) Bonus: change the program so it prints ALL the positions where the word appears
#      and how many times it appears. ("the" -> positions 0 and 15, 2 times)
#
# Answers:
#   a) len(sentence) - len(word). From any later position there aren't enough
#      characters left for the whole word. (So we use range(len(sentence) - len(word) + 1))
#   b) see the bonus code at the end of this question.

sentence = input("Enter a sentence: ")
word = input("Enter a word: ")

found = False
for i in range(len(sentence) - len(word) + 1):   # guess a starting position
    if sentence[i:i + len(word)] == word:         # check
        print(f"Found at index {i}")
        found = True
        break

if not found:
    print("Not found")

# ---- Bonus (b): all the positions ----
sentence = input("Enter a sentence: ")
word = input("Enter a word: ")

count = 0
for i in range(len(sentence) - len(word) + 1):
    if sentence[i:i + len(word)] == word:
        print(f"Found at index {i}")
        count += 1                                # no break - keep searching

if count == 0:
    print("Not found")
else:
    print(f"The word appears {count} times")


############### Q4 ############
# Perfect power 💥
# The program gets a positive integer n and checks whether it is a "perfect power":
# is there an integer root and a power 2 <= pwr <= 5 such that root ** pwr == n ?
# If yes - print one such pair (the smallest power). Otherwise print a message.
#
# Examples:
#   81  ->  81 = 9 ** 2
#   32  ->  32 = 2 ** 5
#   27  ->  27 = 3 ** 3
#   30  ->  30 is not a perfect power (for powers 2-5)
#
# Hint: like the cube-root example from class - for each power, guess root = 1, 2, 3, ...
# and stop guessing as soon as root ** pwr >= n, then check whether you hit n exactly.
# (You will need a loop inside a loop.)
#
# Question for thought: what happens if the user enters 0? Why?
# Answer: range(1, 1) is empty, so the inner loop never runs and "root" is never created
#         -> NameError. A loop variable only exists if the loop ran at least once!

n = int(input("Enter a positive integer: "))

found = False
for pwr in range(2, 6):                 # try powers 2, 3, 4, 5 (smallest first)
    for root in range(1, n + 1):        # guess root = 1, 2, 3, ...
        if root ** pwr >= n:            # passed (or reached) n - no point continuing
            break
    if root ** pwr == n:                # did we hit n exactly?
        print(f"{n} = {root} ** {pwr}")
        found = True
        break

if not found:
    print(f"{n} is not a perfect power (for powers 2-5)")
