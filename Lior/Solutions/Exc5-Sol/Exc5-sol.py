# Created for: Introduction to Programming, Ariel University
# Exercise 5 - SOLUTIONS
# Topic: Tuples and Lists
#
# Every question is independent - run each block on its own.

############### Q1 ############
# Class grades 🎓
# A list of students is stored as a list of TUPLES:  (name, grade)
#
# a) parse_students(lines)   - strings like "Dana,85"  ->  list of (name, grade) tuples
# b) best_student(students)  - the tuple with the highest grade (first one on a tie), no max()
# c) split_pass_fail(students, passing=60)  - returns TWO lists of names: passed, failed
# d) curve(students, bonus)  - returns a NEW list with the bonus added (max 100), original unchanged
#
# Question for thought: Why can't we write  student[1] = student[1] + bonus  inside curve?
#                       What did you do instead?
# Answer: A tuple is IMMUTABLE - we can't change one of its elements.
#         Instead we build a NEW tuple (name, new_grade) for every student and
#         collect the new tuples in a NEW list. The original list and tuples stay as they were.

def parse_students(lines):
    result = []
    for line in lines:
        parts = line.split(",")                 # "Dana,85" -> ["Dana", "85"]
        result.append((parts[0], int(parts[1])))   # the grade is text - convert it to int
    return result


def best_student(students):
    best = students[0]                          # start with the first student
    for student in students:
        if student[1] > best[1]:                # strictly bigger -> on a tie we keep the first
            best = student
    return best


def split_pass_fail(students, passing=60):
    passed = []
    failed = []
    for name, grade in students:                # unpack each tuple into two names
        if grade >= passing:
            passed.append(name)
        else:
            failed.append(name)
    return (passed, failed)                     # ONE value: a tuple of two lists


def curve(students, bonus):
    new_students = []                           # a brand new list - we never touch "students"
    for name, grade in students:
        new_grade = grade + bonus
        if new_grade > 100:
            new_grade = 100
        new_students.append((name, new_grade))  # a new tuple for every student
    return new_students


students = parse_students(["Dana,85", "Omer,52", "Noa,97", "Yossi,60", "Lior,41"])
print(students)       # [('Dana', 85), ('Omer', 52), ('Noa', 97), ('Yossi', 60), ('Lior', 41)]
print(best_student(students))             # ('Noa', 97)

passed, failed = split_pass_fail(students)
print(passed, failed)                     # ['Dana', 'Noa', 'Yossi'] ['Omer', 'Lior']
passed, failed = split_pass_fail(students, 80)
print(passed, failed)                     # ['Dana', 'Noa'] ['Omer', 'Yossi', 'Lior']

new_students = curve(students, 10)
print(new_students)   # [('Dana', 95), ('Omer', 62), ('Noa', 100), ('Yossi', 70), ('Lior', 51)]
print(students)       # [('Dana', 85), ('Omer', 52), ('Noa', 97), ('Yossi', 60), ('Lior', 41)]  - unchanged


############### Q2 ############
# Cleaning lists 🧹
#
# a) remove_all(L, value)  - removes every occurrence of value from L, IN PLACE, returns nothing
# b) without_duplicates(L) - returns a NEW list, each element once, in order of first appearance
# c) What will be printed?
#
# Questions for thought:
#   1) Part (a) is a classic trap: a loop that calls L.remove(...) while going over L
#      doesn't remove everything. What did you do to avoid the problem?
#   2) Why does remove_all return nothing, while without_duplicates must return something?
#   3) In part (c), why did b change but c didn't?
#
# Answers:
#   1) Never change a list while looping over it - when an element is removed, the rest shift left
#      but the loop's hidden position counter moves on, so it skips the next element.
#      Two safe options:
#        - loop over a COPY and remove from the original:   for x in L[:]: ...
#        - don't loop at all:   while value in L: L.remove(value)      (used below)
#   2) remove_all works by SIDE EFFECT: the list the caller gave us IS the list we change
#      (the parameter L is another name for the caller's list), so there's nothing to give back.
#      without_duplicates builds a NEW list - the caller can only get it if we return it.
#   3) b = a   -> b is just a second name for the SAME list, so changing it through a is visible through b.
#      c = a[:] -> c is a CLONE - a separate list with the same elements, so it stays untouched.

def remove_all(L, value):
    while value in L:
        L.remove(value)       # removes the first occurrence each time; changes the caller's list


def without_duplicates(L):
    result = []
    for e in L:
        if e not in result:   # keep only the first appearance
            result.append(e)
    return result


nums = [1, 2, 2, 3, 2]
remove_all(nums, 2)
print(nums)                                # [1, 3]

nums = [2, 2, 2]
remove_all(nums, 2)
print(nums)                                # []

nums = [1, 3]
remove_all(nums, 5)                        # value not in the list - nothing happens
print(nums)                                # [1, 3]

original = [3, 1, 3, 2, 1]
print(without_duplicates(original))        # [3, 1, 2]
print(original)                            # [3, 1, 3, 2, 1]   - unchanged

# Part (c):
a = [1, 2, 2, 3, 2]
b = a
c = a[:]
remove_all(a, 2)
print(a)                                   # [1, 3]
print(b)                                   # [1, 3]
print(c)                                   # [1, 2, 2, 3, 2]
