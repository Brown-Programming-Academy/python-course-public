# Created for: Introduction to Programming, Ariel University
# Homework 4 (optional) - SOLUTIONS
# Topic: Functions
#
# The questions are ordered from easier to harder.
# Every question is independent - run each block on its own.

############### Q1 ############
# Leap years 📅
# a) is_leap(year) returns True / False.
# b) days_in_month(month, year) - uses is_leap for February.
# c) days_in_year(year) - sums the 12 months using days_in_month.
#
# Question for thought:
# Answer: The two answers are computed in different ways. If they agree for many years,
#         it's a good sign that is_leap and days_in_month are both correct -
#         this is a simple way to TEST your own functions.

def is_leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0
    # Also correct in one line:
    # return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(month, year):
    if month == 2:
        if is_leap(year):
            return 29
        return 28
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    return 31


def days_in_year(year):
    total = 0
    for month in range(1, 13):
        total += days_in_month(month, year)
    return total


print(is_leap(2024))            # True
print(is_leap(2026))            # False
print(is_leap(1900))            # False
print(is_leap(2000))            # True
print(days_in_month(1, 2026))   # 31
print(days_in_month(4, 2026))   # 30
print(days_in_month(2, 2024))   # 29
print(days_in_month(2, 2026))   # 28
print(days_in_year(2024))       # 366
print(days_in_year(1900))       # 365


############### Q2 ############
# The most common letter 🔤
#
# Question for thought:
# Answer: most_common_char calls count_char once for every character (n times),
#         and each count_char runs over the whole text (n times) -> about n * n steps.
#         For a text of 1,000,000 characters that is 10^12 steps - way too slow!
#         (Later in the course you'll learn dictionaries, which do it in about n steps.)

def count_char(text, ch):
    count = 0
    for c in text:
        if c == ch:
            count += 1
    return count


def most_common_char(text):
    best = ""
    best_count = 0
    for c in text:
        if c != " ":
            cnt = count_char(text, c)
            if cnt > best_count:   # strictly bigger -> on a tie we keep the first one
                best = c
                best_count = cnt
    return best


print(count_char("banana", "a"))         # 3
print(count_char("banana", "z"))         # 0
print(most_common_char("banana"))        # a
print(most_common_char("hello world"))   # l
print(most_common_char("abcabc"))        # a


############### Q3 ############
# Perfect and friendly numbers 🤝

def sum_proper_divisors(n):
    total = 0
    for d in range(1, n // 2 + 1):   # a proper divisor is never bigger than n / 2
        if n % d == 0:
            total += d
    return total


def is_perfect(n):
    return sum_proper_divisors(n) == n


def are_amicable(a, b):
    return a != b and sum_proper_divisors(a) == b and sum_proper_divisors(b) == a


print(sum_proper_divisors(12))   # 16
print(sum_proper_divisors(7))    # 1
print(is_perfect(28))            # True
print(is_perfect(12))            # False
print(are_amicable(220, 284))    # True
print(are_amicable(6, 6))        # False

# d)
print("Perfect numbers:", end=" ")
for n in range(2, 10001):
    if is_perfect(n):
        print(n, end=" ")
print()

print("Amicable pairs:", end=" ")
for a in range(2, 3001):
    b = sum_proper_divisors(a)      # the only possible friend of a
    if a < b <= 3000 and are_amicable(a, b):   # a < b -> each pair printed once
        print(f"({a}, {b})", end=" ")
print()
