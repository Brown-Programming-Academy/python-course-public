# Created for: Introduction to Programming, Ariel University
# Homework 5 (optional)
# Topic: Tuples and Lists
#
# The questions are ordered from easier to harder.
# Every question is independent - run each block on its own.
#
# General rules for this homework:
#   - Functions should RETURN their answer - not print it!
#     (Printing is done outside the function, by the code that calls it.
#      The only exception is print_matrix in Q2, whose whole job is to print.)
#   - Read each question carefully and notice what the function is allowed to do to its input:
#     some functions must leave the list untouched, others must CHANGE it.

############### Q1 ############
# A toolkit for lists of numbers 📊
# In all parts, the list is not empty.
#
# a) Write a function average(numbers) that RETURNS the average of the numbers.
#    Don't use sum().
#
# b) Write a function above_average(numbers) that RETURNS a NEW list with only the numbers
#    that are bigger than the average, in their original order.
#    Rule: above_average must USE the function average.
#
# c) Write a function min_and_max(numbers) that RETURNS BOTH the smallest and the biggest number.
#    Don't use min() or max().
#
# d) Write a function swap_ends(numbers) that swaps the FIRST and the LAST elements of the list.
#    The function CHANGES the list it received and returns nothing.
#    Do the swap in ONE line (without a temp variable).
#    If the list has fewer than 2 elements - nothing should happen.
#
# Examples:
#   average([4, 8, 6])                 ->  6.0
#   above_average([4, 8, 6, 10, 2])    ->  [8, 10]
#   min_and_max([4, -2, 9, 7])         ->  (-2, 9)
#
#   nums = [1, 2, 3, 4]
#   swap_ends(nums)
#   print(nums)                        ->  [4, 2, 3, 1]
#
# Questions for thought (answer in a comment):
#   a) What does  print(swap_ends(nums))  show? Why?
#   b) above_average gives back a new list, but swap_ends changes the list it received.
#      How can the person who calls each function tell the difference, without reading the code?

# Write your code here


############### Q2 ############
# Matrices 🔢
# A matrix is a table of numbers. We store it as a LIST OF ROWS:
# the matrix is a list, and every element of it is a row - which is itself a list of numbers.
#
#                  column 0   column 1   column 2
#     row 0   ->  [ [  1,        2,         3  ],
#     row 1   ->    [  4,        5,         6  ] ]
#
#     matrix = [[1, 2, 3], [4, 5, 6]]       # 2 rows, 3 columns
#
#   - matrix[i] is ROW number i                       (matrix[1] is [4, 5, 6])
#   - matrix[i][j] is the element in row i, column j  (matrix[1][2] is 6)
#   - COLUMN number j is made of matrix[0][j], matrix[1][j], matrix[2][j], ...
#     (column 2 is 3 and 6)
#   - the number of rows is len(matrix), the number of columns is len(matrix[0])
#
# In all parts: the matrix is not empty and all its rows have the same length.
#
# a) Write a function print_matrix(matrix) that PRINTS the matrix as a table: every row on its
#    own line, with a space between the numbers of the row.
#    (This is the only function in this homework whose job is to print and not to return.)
#
# b) Write a function transpose(matrix) that RETURNS a NEW matrix in which the rows and the
#    columns are swapped: row i of the new matrix is column i of the old one.
#
# c) Write a function multiply_by_scalar(matrix, k) that RETURNS a NEW matrix in which every
#    element is multiplied by the number k.
#
# d) Challenge: write a function multiply(A, B) that RETURNS the product of the matrices A and B.
#
#    How is the product defined?
#    Let A have m rows and n columns, and let B have n rows and p columns
#    (the number of COLUMNS of A must be equal to the number of ROWS of B).
#    The product C = A * B is a matrix with m rows and p columns, where the element
#    in row i and column j is:
#
#        C[i][j] = A[i][0] * B[0][j]  +  A[i][1] * B[1][j]  +  ...  +  A[i][n-1] * B[n-1][j]
#
#    In words: take ROW i of A and COLUMN j of B, multiply the elements that are in the same
#    place, and add everything up.
#
#    Example:  A = [[1, 2],      B = [[5, 6],
#                   [3, 4]]           [7, 8]]
#        C[0][0] = 1*5 + 2*7 = 19        C[0][1] = 1*6 + 2*8 = 22
#        C[1][0] = 3*5 + 4*7 = 43        C[1][1] = 3*6 + 4*8 = 50
#        so  A * B = [[19, 22], [43, 50]]
#
#    If the number of columns of A is different from the number of rows of B,
#    the product is not defined - in that case RETURN None.
#
# All the functions (except print_matrix) must NOT change the matrices they receive.
#
# Examples:
#   matrix = [[1, 2, 3], [4, 5, 6]]
#   print_matrix(matrix)                  prints:
#      1 2 3
#      4 5 6
#   transpose(matrix)                     ->  [[1, 4], [2, 5], [3, 6]]
#   multiply_by_scalar(matrix, 3)         ->  [[3, 6, 9], [12, 15, 18]]
#   multiply([[1, 2], [3, 4]], [[5, 6], [7, 8]])   ->  [[19, 22], [43, 50]]
#   multiply(matrix, transpose(matrix))   ->  [[14, 32], [32, 77]]
#   multiply([[1, 2]], [[1, 2]])          ->  None      (A has 2 columns, but B has only 1 row)
#
# Hints:
#   - For (b) and (c): build the new matrix one row at a time with append.
#   - For (d): the result has len(A) rows and len(B[0]) columns.
#     Build it like this - fill in the "..." yourself:
#
#         result = []
#         for i in range(...):              # every row of A
#             new_row = []
#             for j in range(...):          # every column of B
#                 total = 0
#                 for k in range(...):      # walk along row i of A and down column j of B
#                     total += ...
#                 new_row.append(total)
#             result.append(new_row)
#
# Questions for thought (answer in a comment):
#   1) A student started part (b) like this:
#          result = [[0] * rows] * cols      (and then filled the numbers in)
#      and got a very strange result. Try it with the matrix above.
#      What happened, and why?
#   2) Take A = [[1, 2], [3, 4]] and B = [[0, 1], [1, 0]].
#      Is multiply(A, B) equal to multiply(B, A)? What does it tell you about matrix multiplication?

# Write your code here


############### Q3 ############
# Undo! ↩️
# We are writing the "undo" button of a shopping-list app.
# The shopping list is a list of strings:  items
# Before every change to the list we save a SNAPSHOT (a copy of the list as it was)
# in another list, called history. Undo brings back the latest snapshot.
#
# All the functions CHANGE the lists they receive (and return nothing).
#
# a) Write a function add_item(items, history, item):
#    first save a snapshot of items in history, then add item to the end of items.
#
# b) Write a function remove_item(items, history, item):
#    if item is in items - save a snapshot of items in history, then remove item from items.
#    If item is NOT in items - do nothing at all (and don't save a snapshot).
#
# c) Write a function undo(items, history):
#    take the LAST snapshot out of history, and make items look exactly like it.
#    If history is empty - do nothing.
#
# Test your code like this:
#
#   items = []
#   history = []
#   add_item(items, history, "milk")
#   add_item(items, history, "eggs")
#   add_item(items, history, "bread")
#   print(items)                      ->  ['milk', 'eggs', 'bread']
#   print(len(history))               ->  3
#   remove_item(items, history, "eggs")
#   print(items)                      ->  ['milk', 'bread']
#   remove_item(items, history, "tea")          # not in the list - nothing happens
#   print(len(history))               ->  4
#   undo(items, history)
#   print(items)                      ->  ['milk', 'eggs', 'bread']
#   undo(items, history)
#   print(items)                      ->  ['milk', 'eggs']
#   undo(items, history)
#   undo(items, history)
#   print(items)                      ->  []
#   undo(items, history)                        # nothing left to undo - and no crash!
#   print(items)                      ->  []
#   print(history)                    ->  []
#
# Hints:
#   - A snapshot must be a COPY of the list - not just another name for the same list.
#   - In undo, "last = history.pop()" gives you the latest snapshot.
#     Now items must BECOME last, but it has to be the SAME list object that the caller gave you.
#     The method items.clear() removes all the elements of items (in place),
#     and items.extend(last) adds all the elements of last.
#
# Questions for thought (answer in a comment):
#   1) Another student wrote add_item like this:
#          def add_item(items, history, item):
#              history.append(items)
#              items.append(item)
#      What will  print(history)  show after the three add_item calls of the test above? Why?
#   2) Why wouldn't it work to write  items = history.pop()  inside undo?
#      (Think about what happens to the list that the caller holds.)

# Write your code here
