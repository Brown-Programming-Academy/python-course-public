# Created for: Introduction to Programming, Ariel University
# Exercise 4
# Topic: Functions
#
# Every question is independent - run each block on its own.

############### Q1 ############
# print vs. return 👋
# a) Write a function greet(name) that PRINTS:  Hello <name>!
# b) Write a function make_greeting(name) that RETURNS the string  "Hello <name>!"
#    (and does not print anything).
# c) Call both of them like this and run:
#
#       x = greet("Dana")
#       y = make_greeting("Dana")
#       print(x)
#       print(y)
#
# Question for thought (answer in a comment):
#   What does print(x) show? Why?

# Write your code here


############### Q2 ############
# Building functions from functions 🧱
# Don't use the built-in max().
# a) Write a function max_of_two(a, b) that returns the bigger of the two numbers.
# b) Write a function max_of_three(a, b, c) that returns the biggest of the three.
#    Rule: max_of_three must USE max_of_two (no if inside max_of_three!).
#
# Examples:
#   max_of_two(3, 8)        ->  8
#   max_of_three(4, 9, 2)   ->  9
#   max_of_three(-1, -5, -3) ->  -1

# Write your code here


############### Q3 ############
# Prime numbers - again! 🔢
# In Homework 3 you checked whether a number is prime.
# a) Turn that code into a function is_prime(n) that RETURNS True or False
#    (no printing inside the function!).
# b) Use your function to print all the prime numbers from 1 to 50.
#
# Examples:
#   is_prime(7)   ->  True
#   is_prime(12)  ->  False
#   is_prime(1)   ->  False
#   primes up to 50: 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
#
# Hint: inside a function, "return" ends the function immediately -
#       you can return False as soon as you find a divisor.
#
# Question for thought (answer in a comment):
#   Why is it better that is_prime returns True/False instead of printing?

# Write your code here


############### Q4 ############
# What will be printed? 🕵️ (no code to write - first guess, then run!)
#
# Part A:
x = 10

def change():
    x = 5
    print("inside:", x)

change()
print("outside:", x)

# Part B:
def add_one(n):
    n = n + 1
    return n

a = 3
add_one(a)
print(a)
a = add_one(a)
print(a)

# Questions for thought (answer in a comment):
#   a) Why didn't change() change the x outside?
#   b) Why is the first print(a) 3 and the second 4?


############### Q5 ############
# The Babylonian square root as a function 🏛️
# In Exercise 3 you approximated a square root with:
#     new_guess = (guess + x / guess) / 2
#
# Write a function babylonian_sqrt(x, epsilon=0.0001) that RETURNS the approximation.
#   - start with guess = x
#   - repeat until |guess**2 - x| < epsilon
#   - epsilon has a DEFAULT value: if the caller doesn't pass it, it is 0.0001
#
# Then try:
#   print(babylonian_sqrt(25))           # uses the default epsilon
#   print(babylonian_sqrt(2))
#   print(babylonian_sqrt(2, 0.1))       # less accurate
#   print(babylonian_sqrt(2, epsilon=1e-12))  # very accurate
#
# Question for thought (answer in a comment):
#   Why is it useful to give epsilon a default value?

# Write your code here
