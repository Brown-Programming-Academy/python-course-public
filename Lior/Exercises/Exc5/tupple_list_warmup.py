#   Q1-Q4    tuples
#   Q5-Q6    list indexing and mutation
#   Q7-Q9    list operations (add / remove / strings <-> lists)
#   Q10      sort vs sorted
#   Q11-Q14  aliasing, cloning, nested lists, mutation while iterating


############### Q1 - Tuple basics 🔍 ############
# What will be printed?
t = (5, "hi", 7.5)
print(t[1])                       # hi
print(t[0:2])                     # (5, 'hi')
print(len(t))                     # 3
print(t + (1,))                   # (5, 'hi', 7.5, 1)
print(type((3)), type((3,)))      # <class 'int'> <class 'tuple'>
# Idea: slicing/indexing work like strings. A tuple with ONE element needs a comma.


############### Q2 - Immutable 🔒 ############
# Change the "hi" in t to "bye". Try the obvious way first. Then do it properly.
# Bonus: the same question for the string s = "hello" -> make it "jello".
t = (5, "hi", 7.5)
# >> t[1] = "bye"                 # TypeError: 'tuple' object does not support item assignment
t = (t[0], "bye", t[2])           # build a NEW tuple
print(t)                          # (5, 'bye', 7.5)

s = "hello"
# >> s[0] = "j"                   # TypeError: 'str' object does not support item assignment
s = "j" + s[1:]                   # build a NEW string
print(s)                          # jello
# Idea: immutable = you can't change it, you can only build a new one and move the name.


############### Q3 - Swap 🔄 ############
# a = 3, b = 8. Swap them WITHOUT a temp variable.
# Then: a, b, c = 1, 2, 3  ->  rotate so that a = 2, b = 3, c = 1  (one line).
a = 3
b = 8
a, b = b, a
print(a, b)                       # 8 3

a, b, c = 1, 2, 3
a, b, c = b, c, a
print(a, b, c)                    # 2 3 1
# Idea: the right side is built completely before anything is assigned.


############### Q4 - Return more than one value 📦 ############
# Write rectangle_info(w, h) that returns BOTH the area and the perimeter.
# Call it with 3 and 5 and print the two numbers separately.
def rectangle_info(w, h):
    return (w * h, 2 * (w + h))

area, perimeter = rectangle_info(3, 5)
print(area, perimeter)            # 15 16
print(rectangle_info(3, 5))       # (15, 16)   <- really ONE value: a tuple
# Idea: return a tuple, unpack it with  x, y = f(...)


############### Q5 - List indexing 🔍 ############
# What will be printed?
L = [10, 'a', [1, 2], 4]
i = 3
print(len(L))                     # 4
print(L[2][1])                    # 2          - the inner list's second element
print(L[-1])                      # 4
print(L[1:3])                     # ['a', [1, 2]]
print(L[i - 2])                   # a          - the index can be an expression
# >> print(L[4])                  # IndexError: list index out of range
# Idea: last valid index is len(L) - 1. A list can contain a list.


############### Q6 - Mutating by index ✏️ ############
# Turn every negative number in the list into 0.   [3, -1, 4, -5]  ->  [3, 0, 4, 0]
# ❓ Will "for x in nums: if x < 0: x = 0" work?
nums = [3, -1, 4, -5]
for x in nums:
    if x < 0:
        x = 0
print(nums)                       # [3, -1, 4, -5]   <- NOT changed (x is just a name)

for i in range(len(nums)):
    if nums[i] < 0:
        nums[i] = 0
print(nums)                       # [3, 0, 4, 0]
# Idea: lists are mutable - change them with L[i] = ...  You need the INDEX to do that.


############### Q7 - append / extend / + ➕ ############
# What will be printed?
A = [1, 2]
A.append([3])
A.extend([4, 5])
B = A + [6]
print(A)                          # [1, 2, [3], 4, 5]
print(B)                          # [1, 2, [3], 4, 5, 6]
print(len(A))                     # 5
# Idea: append adds ONE element (even if it's a list). extend adds each element of the other list.
#       Both CHANGE A. "+" builds a NEW list and leaves A alone.


############### Q8 - remove / del / pop ➖ ############
# What will be printed? (the lines depend on each other - go in order)
L = [5, 3, 8, 3, 9, 1]
L.remove(3)
print(L)                          # [5, 8, 3, 9, 1]   - only the FIRST 3 is gone
del L[0]
print(L)                          # [8, 3, 9, 1]
x = L.pop()
print(x, L)                       # 1 [8, 3, 9]
# >> L.remove(100)                # ValueError: list.remove(x): x not in list
# Idea: remove = by value, del = by index, pop = from the end (and gives it back).


############### Q9 - Strings <-> lists 🔤 ############
# Turn "hello big world" into "hello-big-world".   Then turn "abc" into ['a', 'b', 'c'].
text = "hello big world"
words = text.split()              # ['hello', 'big', 'world']
print("-".join(words))            # hello-big-world
print(list("abc"))                # ['a', 'b', 'c']
# >> print("-".join([1, 2, 3]))   # TypeError: sequence item 0: expected str instance, int found
# Idea: split: string -> list.  join: list of STRINGS -> string.


############### Q10 - sort vs sorted ⚖️ ############
# What will be printed?
L = [3, 1, 2]
M = sorted(L)
print(L, M)                       # [3, 1, 2] [1, 2, 3]   - sorted() gives a NEW list
N = L.sort()
print(L, N)                       # [1, 2, 3] None        - sort() changes L and returns None
L.reverse()
print(L)                          # [3, 2, 1]
# Idea: if it changes the list, it returns None - never write  L = L.sort().


############### Q11 - Aliasing 🏷️ ############
# What will be printed?  (use Python Tutor!)
a = [1, 2, 3]
b = a
b[0] = 99
print(a)                          # [99, 2, 3]

def grow(L):
    L.append(0)

def grow_new(L):
    L = L + [0]

x = [1]
grow(x)
print(x)                          # [1, 0]    - the function changed MY list

y = [1]
grow_new(y)
print(y)                          # [1]       - "L = ..." only moved the local name
# Idea: b = a gives the list a SECOND NAME. Changing it through one name shows through the other.


############### Q12 - Cloning 🐑 ############
# This "backup" doesn't work. Fix it so that backup keeps the ORIGINAL data.
data = [4, 5, 6]
backup = data                     # <- the bug
data.append(7)
print(backup)                     # [4, 5, 6, 7]   <- the "backup" changed too

data = [4, 5, 6]
backup = data[:]                  # <- the fix: a new list with the same elements
data.append(7)
print(backup)                     # [4, 5, 6]
print(backup is data, backup == [4, 5, 6])   # False True
# Idea: clone with L[:]  (or list(L), L.copy()).   "==" compares content, "is" asks: same object?


############### Q13 - Lists of lists 🧱 ############
# We want a 2x2 board of zeros, then put a 1 in the top-left corner.
# What will be printed? Then fix it.
board = [[0] * 2] * 2
board[0][0] = 1
print(board)                      # [[1, 0], [1, 0]]   <- BOTH rows changed: they're the same list!

board = []
for _ in range(2):
    board.append([0] * 2)         # a NEW row each time
board[0][0] = 1
print(board)                      # [[1, 0], [0, 0]]
# Idea: "[x] * 2" repeats the SAME object. Inner lists need to be created separately.


############### Q14 - Changing a list while looping over it ⚠️ ############
# Remove all the even numbers from nums.   [2, 4, 6, 1]  ->  expected [1]
nums = [2, 4, 6, 1]
for n in nums:
    if n % 2 == 0:
        nums.remove(n)
print(nums)                       # [4, 1]   <- the 4 survived! The loop skipped it.
# Why: after removing 2 the list shifts left, but the loop's hidden position counter moves on to 1 -> it jumps over 4.

# Fix 1 - loop over a copy:
nums = [2, 4, 6, 1]
for n in nums[:]:
    if n % 2 == 0:
        nums.remove(n)
print(nums)                       # [1]

# Fix 2 - build a new list:
nums = [2, 4, 6, 1]
odds = []
for n in nums:
    if n % 2 != 0:
        odds.append(n)
print(odds)                       # [1]
# Idea: never change a list while looping over it.