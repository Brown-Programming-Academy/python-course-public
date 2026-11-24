# Created for: Introduction to Programming, Ariel University
# Exercise 6
# Topic: Recursion and Dictionaries
#
# Every question is independent - run each block on its own.
#
# General rules:
#   - Functions should RETURN their answer - not print it!
#     (Printing is done outside the function, by the code that calls it.)
#   - In the recursion questions, do not use loops to replace the recursion
#     (where a question says "no loops", it means it).

############### Q1 ############
# Powers ⚡
#
# Write a recursive function power(base, exp) that RETURNS base ** exp.
# Assume exp is an integer >= 0.
# Don't use the ** operator, and don't use loops.
#
# Examples:
#   power(2, 3)  ->  8
#   power(5, 0)  ->  1
#   power(3, 4)  ->  81
#
# Question for thought (answer in a comment):
#   What is the base case of power? What happens if we don't write it?

# Write your code here


############### Q2 ############
# Nested lists 🪆
# A list can contain numbers AND other lists, and those can contain more lists, at any depth.
#
# a) Write a recursive function flatten(L) that RETURNS a NEW flat list with all the numbers,
#    in the same order. The original list must not change.
#
# b) Write a recursive function nesting_depth(L) that RETURNS how deep the deepest list is.
#    A list with no lists inside it has depth 1.
#
# Examples:
#   flatten([1, [2, [3, 4]], 5])      ->  [1, 2, 3, 4, 5]
#   flatten([1, 2, 3])                ->  [1, 2, 3]
#   flatten([[], [[]]])               ->  []
#   flatten([[1, 2], [3, [4, [5, 6]]], 7])  ->  [1, 2, 3, 4, 5, 6, 7]
#
#   nesting_depth([1, 2])             ->  1
#   nesting_depth([1, [2, [3]]])      ->  3
#   nesting_depth([])                 ->  1
#
# Hint: to check if an element is a list use  isinstance(item, list)
#       (it does the same as  type(item) == list)
#
# Questions for thought (answer in a comment):
#   1) Why can't we solve flatten with one for loop, or with a fixed number of nested loops?
#   2) What would  result.append(flatten(item))  give instead of  result = result + flatten(item) ?
#      Try it on [1, [2, 3]].

# Write your code here


############### Q3 ############
# Counting with dictionaries 📊
#
# a) Write a function count_chars(text) that RETURNS a dictionary:
#    every character in text -> how many times it appears.
#
# b) Write a function count_words(sentence) that RETURNS a dictionary:
#    every word in the sentence -> how many times it appears.
#    Words are separated by spaces. Capital letters don't matter ("The" and "the" are the same word).
#
# c) Write a function most_common(counts) that gets a dictionary like the ones above
#    and RETURNS the key with the highest value. If there is a tie, return the first one.
#    Don't use max().
#
# Examples:
#   count_chars("banana")                               ->  {'b': 1, 'a': 3, 'n': 2}
#   count_chars("")                                     ->  {}
#   count_words("the cat and the dog and the bird")     ->  {'the': 3, 'cat': 1, 'and': 2, 'dog': 1, 'bird': 1}
#   count_words("The the THE")                          ->  {'the': 3}
#   most_common(count_words("the cat and the dog and the bird"))  ->  'the'
#   most_common(count_chars("banana"))                  ->  'a'
#
# Question for thought (answer in a comment):
#   What happens if we write  counts[ch] += 1  without checking whether ch is already in the dictionary?
#   Show two different ways to fix it.

# Write your code here


############### Q4 ############
# Folders 📁
# A folder is stored as a dictionary. The key is the name of a file or folder.
# The value is a number if it's a file (its size in KB), or a dictionary if it's a folder
# (with more files and folders inside).
#
#     fs = {
#         "notes.txt": 2,
#         "homework": {"hw1.py": 4, "hw2.py": 6},
#         "photos": {
#             "trip": {"a.jpg": 300, "b.jpg": 250},
#             "me.png": 120,
#         },
#         "empty_folder": {},
#     }
#
# a) Write a recursive function total_size(folder) that RETURNS the total size of all the
#    files in the folder, including everything inside its subfolders.
#
# b) Write a recursive function count_files(folder) that RETURNS how many files (not folders)
#    are in the folder, including its subfolders.
#
# Examples:
#   total_size(fs)                  ->  682
#   total_size(fs["photos"])        ->  670
#   total_size({})                  ->  0
#   count_files(fs)                 ->  6
#
# Question for thought (answer in a comment):
#   Where is the base case in total_size? What happens when it reaches an empty folder?

# Write your code here
