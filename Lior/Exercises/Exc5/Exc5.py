# Created for: Introduction to Programming, Ariel University
# Exercise 5 
# Topic: Tuples and Lists
#
# Every question is independent - run each block on its own.
#
# General rules:
#   - Functions should RETURN their answer - not print it!
#     (Printing is done outside the function, by the code that calls it.)
#   - Pay attention to what each function is allowed to do to its input:
#     some must CHANGE the list they receive, others must leave it untouched.

############### Q1 ############
# Class grades 🎓
# A list of students is stored as a list of TUPLES:  (name, grade)
#     students = [("Dana", 85), ("Omer", 52), ("Noa", 97), ("Yossi", 60), ("Lior", 41)]
#
# a) Write a function parse_students(lines) that gets a list of strings like "Dana,85"
#    and RETURNS a list of (name, grade) tuples. The grade must be an int.
#
# b) Write a function best_student(students) that RETURNS the tuple of the student
#    with the highest grade. (If there is a tie - return the first one.)
#    Don't use max().
#
# c) Write a function split_pass_fail(students, passing=60) that RETURNS TWO lists:
#    the names of the students who passed (grade >= passing), and the names of those who failed.
#    Both lists keep the original order.
#
# d) Write a function curve(students, bonus) that RETURNS a NEW list in which every grade
#    got the bonus added - but no grade may go above 100.
#    The original list must NOT change!
#
# Examples:
#   parse_students(["Dana,85", "Omer,52", "Noa,97"])  ->  [("Dana", 85), ("Omer", 52), ("Noa", 97)]
#   best_student(students)                            ->  ("Noa", 97)
#   split_pass_fail(students)                         ->  (["Dana", "Noa", "Yossi"], ["Omer", "Lior"])
#   split_pass_fail(students, 80)                     ->  (["Dana", "Noa"], ["Omer", "Yossi", "Lior"])
#   curve(students, 10)  ->  [("Dana", 95), ("Omer", 62), ("Noa", 100), ("Yossi", 70), ("Lior", 51)]
#
# Test your code like this:
#   students = parse_students(["Dana,85", "Omer,52", "Noa,97", "Yossi,60", "Lior,41"])
#   print(best_student(students))
#   passed, failed = split_pass_fail(students)
#   print(passed, failed)
#   new_students = curve(students, 10)
#   print(new_students)
#   print(students)      # should still be the original grades!
#
# Question for thought (answer in a comment):
#   Why can't we write  student[1] = student[1] + bonus  inside curve?
#   What did you do instead?

# Write your code here


############### Q2 ############
# Cleaning lists 🧹
#
# a) Write a function remove_all(L, value) that REMOVES every occurrence of value from the
#    list L - IN PLACE (the list that the caller gave you must change).
#    The function returns nothing.
#
# b) Write a function without_duplicates(L) that RETURNS a NEW list with every element
#    appearing only once, in the order of its FIRST appearance.
#    The original list must NOT change.
#
# Examples:
#   nums = [1, 2, 2, 3, 2]
#   remove_all(nums, 2)
#   print(nums)                          ->  [1, 3]
#
#   nums = [2, 2, 2]
#   remove_all(nums, 2)
#   print(nums)                          ->  []
#
#   without_duplicates([3, 1, 3, 2, 1])  ->  [3, 1, 2]
#
# c) What will be printed? (no code to write - first guess, then run!)
#
#       a = [1, 2, 2, 3, 2]
#       b = a
#       c = a[:]
#       remove_all(a, 2)
#       print(a)
#       print(b)
#       print(c)
#
# Questions for thought (answer in a comment):
#   1) Part (a) is a classic trap: a loop that calls L.remove(...) while going over L
#      doesn't remove everything. What did you do to avoid the problem?
#   2) Why does remove_all return nothing, while without_duplicates must return something?
#   3) In part (c), why did b change but c didn't?

# Write your code here
