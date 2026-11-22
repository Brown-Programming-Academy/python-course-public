# Created for: Introduction to Programming, Ariel University
# Homework 5 (optional) - SOLUTIONS
# Topic: Tuples and Lists
#
# The questions are ordered from easier to harder.
# Every question is independent - run each block on its own.

############### Q1 ############
# A toolkit for lists of numbers 📊
# a) average(numbers)        - RETURNS the average, without sum().
# b) above_average(numbers)  - RETURNS a NEW list of the numbers above the average; uses average.
# c) min_and_max(numbers)    - RETURNS (smallest, biggest), without min() / max().
# d) swap_ends(numbers)      - swaps the first and last elements IN PLACE, returns nothing.
#
# Questions for thought:
#   a) What does  print(swap_ends(nums))  show? Why?
#   b) How can the caller tell the difference between a function that returns a new list
#      and a function that changes the list it received?
#
# Answers:
#   a) None. swap_ends has no return statement, so Python returns None automatically.
#      The list WAS changed - but by a side effect, not through the return value.
#   b) Without reading the code, the caller can look at what the function returns:
#      a function that changes the list in place returns None (like append, sort, remove),
#      while a function that builds a new list returns that list.
#      That's also why good functions say in a comment which of the two they do.

def average(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)


def above_average(numbers):
    avg = average(numbers)            # computed ONCE, before the loop
    result = []                       # a new list - the original stays untouched
    for n in numbers:
        if n > avg:
            result.append(n)
    return result


def min_and_max(numbers):
    smallest = numbers[0]
    biggest = numbers[0]
    for n in numbers:
        if n < smallest:
            smallest = n
        if n > biggest:
            biggest = n
    return (smallest, biggest)        # ONE value: a tuple of two numbers


def swap_ends(numbers):
    if len(numbers) >= 2:
        numbers[0], numbers[-1] = numbers[-1], numbers[0]   # no temp variable needed
    # no return - the list itself was changed


print(average([4, 8, 6]))                  # 6.0
print(above_average([4, 8, 6, 10, 2]))     # [8, 10]
print(min_and_max([4, -2, 9, 7]))          # (-2, 9)
lowest, highest = min_and_max([4, -2, 9, 7])
print(lowest, highest)                     # -2 9

nums = [1, 2, 3, 4]
swap_ends(nums)
print(nums)                                # [4, 2, 3, 1]

single = [7]
swap_ends(single)                          # fewer than 2 elements - nothing happens
print(single)                              # [7]

print(swap_ends(nums))                     # None   (and nums is swapped back: [1, 2, 3, 4])
print(nums)                                # [1, 2, 3, 4]


############### Q2 ############
# Matrices 🔢
# a) print_matrix(matrix)           - PRINTS the table, every row on its own line
# b) transpose(matrix)              - a NEW matrix, rows and columns swapped
# c) multiply_by_scalar(matrix, k)  - a NEW matrix, every element times k
# d) multiply(A, B)                 - the matrix product; None if the sizes don't fit
#
#    C[i][j] = A[i][0]*B[0][j] + A[i][1]*B[1][j] + ... + A[i][n-1]*B[n-1][j]
#    (row i of A against column j of B)
#
# Questions for thought:
#   1) A student started part (b) like this:   result = [[0] * rows] * cols
#      What happened, and why?
#   2) Is multiply(A, B) equal to multiply(B, A) for A = [[1, 2], [3, 4]], B = [[0, 1], [1, 0]]?
#
# Answers:
#   1) All the rows of result are the SAME list - "[x] * n" repeats the very same object n times
#      (it doesn't create n separate lists). So when we write a number into result[0][1],
#      we see it in EVERY row:
#          result = [[0] * 2] * 3
#          result[0][1] = 4      ->  [[0, 4], [0, 4], [0, 4]]
#      The fix: create every row separately inside a loop (new_row = [] and result.append(new_row)).
#   2) No: multiply(A, B) is [[2, 1], [4, 3]] but multiply(B, A) is [[3, 4], [1, 2]].
#      Matrix multiplication is NOT commutative - the order matters (unlike multiplying regular numbers).

def print_matrix(matrix):
    for row in matrix:
        line = ""                        # we build the text of one row...
        for x in row:
            line += str(x)               # str() turns the number into text
            line += " "                  # a space after every number
        print(line)                      # ...and print it: one row = one line


def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = []
    for j in range(cols):                # every column of the old matrix...
        new_row = []                     # ...becomes a NEW row
        for i in range(rows):
            new_row.append(matrix[i][j])
        result.append(new_row)
    return result


def multiply_by_scalar(matrix, k):
    result = []
    for row in matrix:
        new_row = []                     # a new row for every old row - the original is untouched
        for x in row:
            new_row.append(x * k)
        result.append(new_row)
    return result


def multiply(A, B):
    if len(A[0]) != len(B):              # columns of A must equal rows of B
        return None
    result = []
    for i in range(len(A)):              # every row of A
        new_row = []
        for j in range(len(B[0])):       # every column of B
            total = 0
            for k in range(len(B)):      # walk along row i of A and down column j of B
                total += A[i][k] * B[k][j]
            new_row.append(total)
        result.append(new_row)
    return result


matrix = [[1, 2, 3], [4, 5, 6]]
print_matrix(matrix)
# 1 2 3
# 4 5 6
print(transpose(matrix))                 # [[1, 4], [2, 5], [3, 6]]
print(multiply_by_scalar(matrix, 3))     # [[3, 6, 9], [12, 15, 18]]
print(matrix)                            # [[1, 2, 3], [4, 5, 6]]   - unchanged

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print(multiply(A, B))                    # [[19, 22], [43, 50]]
print(multiply(matrix, transpose(matrix)))   # [[14, 32], [32, 77]]
print(multiply([[1, 2]], [[1, 2]]))      # None
print_matrix(multiply(A, B))
# 19 22
# 43 50

# Question for thought 1 - the strange result:
result = [[0] * 2] * 3
result[0][1] = 4
print(result)                            # [[0, 4], [0, 4], [0, 4]]

# Question for thought 2 - the order matters:
P = [[1, 2], [3, 4]]
Q = [[0, 1], [1, 0]]
print(multiply(P, Q))                    # [[2, 1], [4, 3]]
print(multiply(Q, P))                    # [[3, 4], [1, 2]]


############### Q3 ############
# Undo! ↩️
# a) add_item(items, history, item)     - snapshot, then add
# b) remove_item(items, history, item)  - if it's there: snapshot, then remove; otherwise nothing
# c) undo(items, history)               - bring back the latest snapshot (IN PLACE)
#
# Questions for thought:
#   1) What will print(history) show if add_item uses  history.append(items)  without a copy?
#   2) Why wouldn't  items = history.pop()  work inside undo?
#
# Answers:
#   1) [['milk', 'eggs', 'bread'], ['milk', 'eggs', 'bread'], ['milk', 'eggs', 'bread']]
#      history.append(items) doesn't save a copy - it saves ANOTHER NAME for the same list.
#      All the "snapshots" are the very same list as items, so they always show its current
#      content. The snapshots change together with the list - and then undo can't bring anything back.
#      That's why we clone:  history.append(items[:])
#   2) Inside the function, items is a local name that points to the caller's list.
#      "items = history.pop()" only moves the LOCAL name to point at the snapshot -
#      the caller's list is not touched, so the caller sees no undo at all.
#      To change the caller's list we must change the object itself: clear() it and extend() it.

def add_item(items, history, item):
    history.append(items[:])        # a COPY of the list as it is now
    items.append(item)


def remove_item(items, history, item):
    if item in items:
        history.append(items[:])    # snapshot only if something is going to change
        items.remove(item)


def undo(items, history):
    if len(history) > 0:
        last = history.pop()        # the latest snapshot (and it's removed from history)
        items.clear()               # empty the caller's list - in place
        items.extend(last)          # and fill it with the snapshot's elements


items = []
history = []
add_item(items, history, "milk")
add_item(items, history, "eggs")
add_item(items, history, "bread")
print(items)                        # ['milk', 'eggs', 'bread']
print(len(history))                 # 3
remove_item(items, history, "eggs")
print(items)                        # ['milk', 'bread']
remove_item(items, history, "tea")  # not in the list - nothing happens
print(len(history))                 # 4
undo(items, history)
print(items)                        # ['milk', 'eggs', 'bread']
undo(items, history)
print(items)                        # ['milk', 'eggs']
undo(items, history)
undo(items, history)
print(items)                        # []
undo(items, history)                # nothing left to undo - no crash
print(items)                        # []
print(history)                      # []

# The buggy version from the question for thought:
def add_item_buggy(items, history, item):
    history.append(items)           # no copy!
    items.append(item)

items = []
history = []
add_item_buggy(items, history, "milk")
add_item_buggy(items, history, "eggs")
add_item_buggy(items, history, "bread")
print(history)   # [['milk', 'eggs', 'bread'], ['milk', 'eggs', 'bread'], ['milk', 'eggs', 'bread']]
