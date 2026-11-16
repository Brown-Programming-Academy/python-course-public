# Created for: Introduction to Programming, Ariel University
# Exercise 4 - SOLUTIONS
# Topic: Functions
#
# Every question is independent - run each block on its own.

############### Q1 ############
# print vs. return 👋
# a) Write a function greet(name) that PRINTS:  Hello <name>!
# b) Write a function make_greeting(name) that RETURNS the string  "Hello <name>!"
#    (and does not print anything).
# c) Call both of them and print the results.
#
# Question for thought: What does print(x) show? Why?
# Answer: None. greet() has no return, so Python returns None automatically.
#         It printed "Hello Dana!" while running - but it gave nothing back.
#         Printing shows something to the user; returning gives a value back to the code.

def greet(name):
    print(f"Hello {name}!")


def make_greeting(name):
    return f"Hello {name}!"


x = greet("Dana")          # prints Hello Dana!
y = make_greeting("Dana")  # prints nothing
print(x)                   # None
print(y)                   # Hello Dana!


############### Q2 ############
# Building functions from functions 🧱
# Don't use the built-in max().
# a) max_of_two(a, b) returns the bigger of the two numbers.
# b) max_of_three(a, b, c) returns the biggest - and must USE max_of_two.

def max_of_two(a, b):
    if a > b:
        return a
    return b               # we only get here if a > b was False


def max_of_three(a, b, c):
    return max_of_two(max_of_two(a, b), c)   # the result of one call goes into another


print(max_of_two(3, 8))          # 8
print(max_of_three(4, 9, 2))     # 9
print(max_of_three(-1, -5, -3))  # -1


############### Q3 ############
# Prime numbers - again! 🔢
# a) is_prime(n) returns True or False (no printing inside).
# b) Use it to print all the primes from 1 to 50.
#
# Question for thought: Why is it better that is_prime returns True/False instead of printing?
# Answer: Because then we can REUSE it - in an if, in a loop, in another function.
#         A function that prints can only show text; we couldn't use it in part (b).

def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False   # found a divisor - return ends the function right here
        d += 1
    return True            # no divisor found


print(is_prime(7))    # True
print(is_prime(12))   # False
print(is_prime(1))    # False

for num in range(1, 51):
    if is_prime(num):
        print(num, end=" ")
print()


############### Q4 ############
# What will be printed? 🕵️
#
# Output:
#   inside: 5
#   outside: 10
#   3
#   4
#
# Answers:
#   a) x = 5 inside the function creates a NEW, LOCAL variable that lives only
#      inside change(). The global x is a different variable - it stays 10.
#   b) n is a local copy of the value of a. Changing n doesn't touch a.
#      The first call returns 4, but nobody saves it - the value is lost.
#      Only "a = add_one(a)" stores the returned value back in a.

x = 10

def change():
    x = 5
    print("inside:", x)

change()
print("outside:", x)

def add_one(n):
    n = n + 1
    return n

a = 3
add_one(a)
print(a)
a = add_one(a)
print(a)


############### Q5 ############
# The Babylonian square root as a function 🏛️
#
# Question for thought: Why is it useful to give epsilon a default value?
# Answer: Most callers just want "a good answer" and shouldn't have to think about
#         epsilon. Those who need more (or less) accuracy can still pass their own.

def babylonian_sqrt(x, epsilon=0.0001):
    guess = x
    while abs(guess ** 2 - x) >= epsilon:
        guess = (guess + x / guess) / 2
    return guess


print(babylonian_sqrt(25))                 # 5.000000000053722
print(babylonian_sqrt(2))                  # 1.4142156862745097
print(babylonian_sqrt(2, 0.1))             # 1.4166666666666665
print(babylonian_sqrt(2, epsilon=1e-12))   # 1.414213562373095
