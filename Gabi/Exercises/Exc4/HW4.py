# Created for: Introduction to Programming, Ariel University
# Homework 4 (optional)
# Topic: Functions
#
# The questions are ordered from easier to harder.
# Every question is independent - run each block on its own.
#
# General rule for this homework:
#   Functions should RETURN their answer - not print it!
#   (Printing is done outside the function, by the code that calls it.)

############### Q1 ############
# Leap years 📅
# Background:
#   A year is a LEAP year (has February 29) if:
#     - it is divisible by 4,
#     - EXCEPT years divisible by 100 - those are NOT leap years,
#     - EXCEPT years divisible by 400 - those ARE leap years after all.
#
# a) Write a function is_leap(year) that RETURNS True or False.
# b) Write a function days_in_month(month, year) that RETURNS how many days
#    the month has (month is a number 1-12).
#    Rule: days_in_month must use is_leap for February.
# c) Write a function days_in_year(year) that RETURNS 365 or 366.
#    Rule: days_in_year must use days_in_month (sum the 12 months with a loop).
#
# Examples:
#   is_leap(2024)            ->  True
#   is_leap(2026)            ->  False
#   is_leap(1900)            ->  False   (divisible by 100)
#   is_leap(2000)            ->  True    (divisible by 400)
#   days_in_month(1, 2026)   ->  31
#   days_in_month(4, 2026)   ->  30
#   days_in_month(2, 2024)   ->  29
#   days_in_month(2, 2026)   ->  28
#   days_in_year(2024)       ->  366
#   days_in_year(1900)       ->  365
#
# Hint: months 4, 6, 9 and 11 have 30 days; February is special; all the rest have 31.
#
# Question for thought (answer in a comment):
#   Part (c) could be solved with just an if on is_leap(year) (366 or 365).
#   Why is it still a nice check that summing the months gives the same answer?

# Write your code here


############### Q2 ############
# The most common letter 🔤
# a) Write a function count_char(text, ch) that RETURNS how many times
#    the character ch appears in text.
#    You may NOT use text.count() - use a loop.
# b) Write a function most_common_char(text) that RETURNS the character that
#    appears the most times in text. Ignore spaces.
#    If there is a tie - return the one that appears FIRST in the text.
#    Rule: most_common_char must use count_char.
#
# Examples:
#   count_char("banana", "a")              ->  3
#   count_char("banana", "z")              ->  0
#   most_common_char("banana")             ->  'a'
#   most_common_char("hello world")        ->  'l'
#   most_common_char("abcabc")             ->  'a'   (tie - 'a' comes first)
#
# Question for thought (answer in a comment):
#   For a text of length n, about how many times does the loop inside count_char
#   run in total when we call most_common_char? Could this be a problem for a very long text?

# Write your code here


############### Q3 ############
# Perfect and friendly numbers 🤝
# Background:
#   The proper divisors of n are all its divisors except n itself.
#     proper divisors of 12: 1, 2, 3, 4, 6   ->  sum = 16
#   A PERFECT number equals the sum of its proper divisors.
#     6 = 1 + 2 + 3   ->  6 is perfect
#   Two different numbers a and b are AMICABLE ("friendly") if
#   the sum of the proper divisors of a is b, AND the sum of the proper divisors of b is a.
#     220 -> 1+2+4+5+10+11+20+22+44+55+110 = 284
#     284 -> 1+2+4+71+142 = 220             ->  220 and 284 are amicable
#
# a) Write a function sum_proper_divisors(n) that returns the sum of the proper divisors of n.
# b) Write a function is_perfect(n) that returns True / False.
# c) Write a function are_amicable(a, b) that returns True / False.
#    (Remember: a and b must be different!)
# d) Use your functions to print:
#    - all the perfect numbers up to 10000
#    - all the amicable pairs where both numbers are up to 3000 (print each pair once!)
#
# Examples:
#   sum_proper_divisors(12)    ->  16
#   sum_proper_divisors(7)     ->  1
#   is_perfect(28)             ->  True
#   is_perfect(12)             ->  False
#   are_amicable(220, 284)     ->  True
#   are_amicable(6, 6)         ->  False
#
# Expected output for (d):
#   Perfect numbers: 6 28 496 8128
#   Amicable pairs: (220, 284) (1184, 1210) (2620, 2924)
#
# Hint for (d): for each a, you don't need to try every b -
#   the only possible friend of a is b = sum_proper_divisors(a).

# Write your code here
