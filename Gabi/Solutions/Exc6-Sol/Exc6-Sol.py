# Created for: Introduction to Programming, Ariel University
# Exercise 6 - SOLUTIONS
# Topic: Recursion and Dictionaries
#
# Every question is independent - run each block on its own.

############### Q1 ############
# Powers ⚡
#
# power(base, exp)  - recursive base ** exp, no ** and no loops
#
# Question for thought:
#   What is the base case of power? What happens if we don't write it?
#
# Answer: The base case is exp == 0 (the answer is 1). Without it the function keeps calling itself
#   with exp = -1, -2, ... and never stops, until Python gives up with a RecursionError.

def power(base, exp):
    if exp == 0:                            # base case
        return 1
    return base * power(base, exp - 1)      # the same problem with a smaller exponent


print(power(2, 3))      # 8
print(power(5, 0))      # 1
print(power(3, 4))      # 81


############### Q2 ############
# Nested lists 🪆
#
# a) flatten(L)        - a NEW flat list with all the numbers, same order
# b) nesting_depth(L)  - how deep the deepest list is (a list with no lists inside has depth 1)
#
# Questions for thought:
#   1) Why can't we solve flatten with one for loop, or with a fixed number of nested loops?
#   2) What would  result.append(flatten(item))  give instead of  result = result + flatten(item) ?
#
# Answers:
#   1) We don't know in advance how deep the lists go. A for loop handles one level, two nested loops
#      handle two levels, and so on - a list with a deeper nesting breaks it.
#      Recursion handles any depth: every inner list is solved by the same function.
#   2) append adds the returned list as ONE element, so the result stays nested:
#      for [1, [2, 3]] we would get [1, [2, 3]] and not [1, 2, 3].
#      "+" joins the two lists into one.

def flatten(L):
    result = []                                 # a new list - the original is never changed
    for item in L:
        if isinstance(item, list):              # same as: type(item) == list
            result = result + flatten(item)     # a list -> flatten it and join the answer
        else:
            result.append(item)                 # a number -> just add it
    return result


def nesting_depth(L):
    deepest = 0
    for item in L:
        if isinstance(item, list):              # same as: type(item) == list
            d = nesting_depth(item)             # depth of the inner list
            if d > deepest:
                deepest = d
    return deepest + 1                          # +1 for the list we are in


print(flatten([1, [2, [3, 4]], 5]))                 # [1, 2, 3, 4, 5]
print(flatten([1, 2, 3]))                           # [1, 2, 3]
print(flatten([[], [[]]]))                          # []
print(flatten([[1, 2], [3, [4, [5, 6]]], 7]))       # [1, 2, 3, 4, 5, 6, 7]

original = [1, [2, 3]]
flatten(original)
print(original)                                     # [1, [2, 3]]   - unchanged

print(nesting_depth([1, 2]))                        # 1
print(nesting_depth([1, [2, [3]]]))                 # 3
print(nesting_depth([]))                            # 1


############### Q3 ############
# Counting with dictionaries 📊
#
# a) count_chars(text)       - dictionary: character -> how many times it appears
# b) count_words(sentence)   - dictionary: word -> how many times (capital letters don't matter)
# c) most_common(counts)     - the key with the highest value, first one on a tie, no max()
#
# Question for thought:
#   What happens if we write  counts[ch] += 1  without checking whether ch is already in the dictionary?
#   Show two different ways to fix it.
#
# Answer: The first time we see a character it is not a key yet, so  counts[ch] += 1  tries to read
#   a value that doesn't exist and crashes with a KeyError.
#   Fix 1 (used in count_chars): check with "in" - if it's there add 1, otherwise create it with 1.
#   Fix 2 (used in count_words): counts[ch] = counts.get(ch, 0) + 1
#   get returns 0 when the key is missing, so the same line works for new and existing keys.

def count_chars(text):
    counts = {}
    for ch in text:
        if ch in counts:
            counts[ch] += 1         # seen before - add one
        else:
            counts[ch] = 1          # first time - create it
    return counts


def count_words(sentence):
    counts = {}
    for word in sentence.lower().split():       # lower() so "The" and "the" are the same word
        counts[word] = counts.get(word, 0) + 1
    return counts


def most_common(counts):
    best_key = None
    best = 0
    for key in counts:
        if counts[key] > best:      # strictly bigger -> on a tie we keep the first
            best = counts[key]
            best_key = key
    return best_key


print(count_chars("banana"))        # {'b': 1, 'a': 3, 'n': 2}
print(count_chars(""))              # {}
print(count_words("the cat and the dog and the bird"))
# {'the': 3, 'cat': 1, 'and': 2, 'dog': 1, 'bird': 1}
print(count_words("The the THE"))   # {'the': 3}
print(most_common(count_words("the cat and the dog and the bird")))     # the
print(most_common(count_chars("banana")))                               # a
print(most_common({"x": 2, "y": 2}))                                    # x   (tie - the first one)


############### Q4 ############
# Folders 📁
# A folder is a dictionary: name -> a number (a file, its size in KB) or a dictionary (a folder).
#
# a) total_size(folder)   - total size of all the files, including subfolders
# b) count_files(folder)  - how many files (not folders), including subfolders
#
# Question for thought:
#   Where is the base case in total_size? What happens when it reaches an empty folder?
#
# Answer: There is no separate "if" for the base case. The base case is a folder with no subfolders
#   (or an empty one): the loop never reaches the recursive call, so the function simply returns.
#   An empty folder has nothing to loop over, so total_size returns 0.

fs = {
    "notes.txt": 2,
    "homework": {"hw1.py": 4, "hw2.py": 6},
    "photos": {
        "trip": {"a.jpg": 300, "b.jpg": 250},
        "me.png": 120,
    },
    "empty_folder": {},
}


def total_size(folder):
    total = 0
    for name in folder:                     # the loop gives the names (keys)
        value = folder[name]
        if isinstance(value, dict):         # same as: type(value) == dict
            total += total_size(value)      # a folder -> add the size of everything inside it
        else:
            total += value                  # a file -> add its size
    return total


def count_files(folder):
    count = 0
    for name in folder:
        value = folder[name]
        if isinstance(value, dict):         # same as: type(value) == dict
            count += count_files(value)     # a folder -> count the files inside it
        else:
            count += 1                      # a file -> one more file
    return count


print(total_size(fs))               # 682
print(total_size(fs["photos"]))     # 670
print(total_size({}))               # 0
print(count_files(fs))              # 6
print(count_files(fs["homework"]))  # 2
print(count_files({}))              # 0
