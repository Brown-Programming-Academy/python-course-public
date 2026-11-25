# Created for: Introduction to Programming, Ariel University
# Homework 6 (optional) - SOLUTIONS
# Topic: Recursion and Dictionaries
#
# Every question is independent - run each block on its own.

############### Q1 ############
# Happy numbers 😊
# a) sum_square_digits(n)  - recursive: the sum of the squares of the digits of n
# b) is_happy(n)           - recursive: True if n is happy (reaches 1), False if it goes in a circle
#
# Questions for thought:
#   1) Try is_happy(2) with a version that has no list of seen numbers. What happens? Why?
#   2) For is_happy(19), what is the list of seen numbers when the helper reaches 1?
#
# Answers:
#   1) RecursionError. 2 is unhappy: 2 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4 -> ...
#      the numbers repeat forever, and the only base case ("n == 1") is never reached.
#      Every call waits for the next one, the calls pile up, and Python stops the program.
#      The list of seen numbers gives us a second base case: a number that is already in the list
#      means we are going around in a circle, so the number can't be happy.
#   2) [19, 82, 68, 100]  - all the numbers we passed through before reaching 1.

def sum_square_digits(n):
    if n == 0:                                  # no digits left
        return 0
    last = n % 10                               # the last digit
    return last * last + sum_square_digits(n // 10)    # + the same for the rest of the number


def is_happy_helper(n, seen):
    if n == 1:                                  # base case 1: we reached 1 - happy
        return True
    if n in seen:                               # base case 2: we have been here before - a circle
        return False
    return is_happy_helper(sum_square_digits(n), seen + [n])   # seen + [n] is a NEW list with n added


def is_happy(n):
    return is_happy_helper(n, [])               # we start with nothing seen


print(sum_square_digits(19))     # 82
print(sum_square_digits(123))    # 14
print(sum_square_digits(7))      # 49
print(sum_square_digits(0))      # 0

print(is_happy(1))               # True
print(is_happy(7))               # True
print(is_happy(19))              # True
print(is_happy(100))             # True
print(is_happy(2))               # False
print(is_happy(4))               # False
print(is_happy(15))              # False


############### Q2 ############
# Binary numbers 💻
# a) to_binary(n)   - recursive: the binary form of n, as a string
# b) count_ones(n)  - recursive: how many 1s there are in the binary form of n
#
# Questions for thought:
#   1) What is the base case of to_binary?
#   2) What would to_binary(10) return if the last digit were written BEFORE the recursive call?
#
# Answers:
#   1) n < 2 (that is 0 or 1): the binary form is just the number itself, as a string.
#      Without the base case n keeps getting halved: ... 1, 0, 0, 0, ... and the calls never stop.
#   2) "0101" instead of "1010" - the digits come out in the REVERSE order.
#      The recursive call returns the digits of the "rest" of the number, and the last digit has to
#      be added after them (on the right). If we add it first, it ends up on the left.
#      (Try:  str(n % 2) + to_binary(n // 2)  for n = 10.)

def to_binary(n):
    if n < 2:                                   # base case: 0 -> "0", 1 -> "1"
        return str(n)
    return to_binary(n // 2) + str(n % 2)       # the digits of the rest, then the last digit


def count_ones(n):
    if n == 0:                                  # no digits left, no ones
        return 0
    return n % 2 + count_ones(n // 2)           # the last digit is 1 or 0 - it counts itself


print(to_binary(0))      # 0
print(to_binary(1))      # 1
print(to_binary(10))     # 1010
print(to_binary(13))     # 1101
print(to_binary(255))    # 11111111

print(count_ones(0))     # 0
print(count_ones(8))     # 1
print(count_ones(13))    # 3
print(count_ones(255))   # 8

# Question for thought 2 - the digits in the wrong order:
def to_binary_wrong(n):
    if n < 2:
        return str(n)
    return str(n % 2) + to_binary_wrong(n // 2)

print(to_binary_wrong(10))    # 0101


############### Q3 ############
# Boxes inside boxes 📦
# A box is a list. Inside it there are numbers and other boxes, at any depth.
# a) sum_nested(box)   - the sum of ALL the numbers, at every depth
# b) count_boxes(box)  - how many boxes (lists) in total, including the box itself
#
# Questions for thought:
#   1) What does sum_nested return for an empty box? Do you need a special "if" for it?
#   2) In count_boxes, why do we start counting from 1 and not from 0?
#
# Answers:
#   1) 0. There is no special "if": the for loop has nothing to go over, so it never runs
#      and the function returns the 0 it started with. The base case is "hidden" -
#      a box that has no boxes inside it never reaches the recursive call.
#   2) The box we are in is also a box, and the loop only counts the boxes INSIDE it.
#      So we start from 1 for the box itself, and add the boxes of every inner box.

def sum_nested(box):
    total = 0
    for item in box:
        if isinstance(item, list):              # same as: type(item) == list
            total += sum_nested(item)           # a box -> add everything inside it
        else:
            total += item                       # a number -> add it
    return total


def count_boxes(box):
    count = 1                                   # this box itself
    for item in box:
        if isinstance(item, list):              # same as: type(item) == list
            count += count_boxes(item)          # a box -> add all the boxes inside it (and itself)
    return count


print(sum_nested([1, [2, 3], [4, [5]]]))    # 15
print(sum_nested([10, [20, [30]]]))         # 60
print(sum_nested([]))                       # 0
print(sum_nested([[], [[]]]))               # 0

print(count_boxes([1, [2, 3], [4, [5]]]))   # 4
print(count_boxes([1, 2, 3]))               # 1
print(count_boxes([]))                      # 1
print(count_boxes([[], [[]]]))              # 4


############### Q4 ############
# A small shop 🛒
# a) a short program that does a few things to a dictionary (see the output below)
# b) total_cost(prices, basket)    - the total price of the basket; unknown products cost 0
# c) expensive_items(prices, limit) - a list of the names of products that cost MORE than limit
#
# Questions for thought:
#   1) What happens if you write prices["cheese"] for a product that is not in the shop?
#      How did you avoid this in total_cost?
#   2) In part (c), what do you get when you go over the dictionary with  for name in prices ?
#      How did you get the price?
#
# Answers:
#   1) A KeyError - the program crashes, because there is no such key.
#      In total_cost we used  prices.get(product, 0)  - it returns 0 when the key is missing,
#      so a product that isn't sold simply costs 0. (Another way: check  if product in prices  first.)
#   2) A for loop over a dictionary gives the KEYS - the names of the products.
#      The price is  prices[name].  (Or:  for name, price in prices.items()  gives both at once.)

# Part (a):
prices = {"apple": 3, "banana": 2, "milk": 7}      # 1) create
print(prices["milk"])                              # 2) 7
prices["bread"] = 5                                # 3) a new key - adds an entry
prices["apple"] = 4                                # 4) an existing key - changes the value
print("cheese" in prices)                          # 5) False
del prices["banana"]                               # 6) delete
print(len(prices))                                 # 7) 3
for name in prices:                                # 8) the loop gives the keys
    print(name, "costs", prices[name])
# apple costs 4
# milk costs 7
# bread costs 5


def total_cost(prices, basket):
    total = 0
    for product in basket:
        total += prices.get(product, 0)            # 0 if the product is not sold
    return total


def expensive_items(prices, limit):
    result = []
    for name in prices:                            # the keys
        if prices[name] > limit:                   # the value of this key
            result.append(name)
    return result


prices = {"apple": 3, "banana": 2, "milk": 7}      # the original prices
print(total_cost(prices, ["apple", "milk", "apple"]))   # 13
print(total_cost(prices, ["bread", "milk"]))            # 7
print(total_cost(prices, []))                           # 0
print(expensive_items(prices, 2))                       # ['apple', 'milk']
print(expensive_items(prices, 10))                      # []


############### Q5 ############
# Translator 🌍
# a) translate(sentence, words)  - translate every word that is in the dictionary, keep the others
# b) invert(words)               - a NEW dictionary with the keys and the values swapped
# c) group_by_length(words)      - a dictionary: length -> list of the words of that length
#
# Questions for thought:
#   1) In translate, why is  words.get(word, word)  a good choice? What does the second "word" do?
#   2) What happens in invert if two English words have the same Spanish translation?
#
# Answers:
#   1) get(word, default) returns the translation if the word is in the dictionary, and the default
#      if it isn't. The second "word" is the default: a word we can't translate stays as it was.
#      It replaces an "if word in words ... else ..." with one short line.
#   2) Keys are unique, so only one of them survives. For {"a": "x", "b": "x"} the result is {"x": "b"}:
#      the loop first writes result["x"] = "a", and then result["x"] = "b" replaces it.
#      That's why the question promises that all the values are different.

def translate(sentence, words):
    result = []
    for word in sentence.split():
        result.append(words.get(word, word))       # the translation, or the word itself
    return " ".join(result)


def invert(words):
    result = {}
    for key in words:
        result[words[key]] = key                   # the value becomes the key, and the key the value
    return result


def group_by_length(words):
    groups = {}
    for word in words:
        n = len(word)
        if n in groups:
            groups[n].append(word)                 # the value is a list - we add to it
        else:
            groups[n] = [word]                     # the first word of this length: a new list
    return groups


words = {"the": "el", "cat": "gato", "dog": "perro", "hello": "hola"}
print(translate("the cat and the dog", words))     # el gato and el perro
print(translate("hello", words))                   # hola
print(translate("good morning", words))            # good morning

print(invert(words))               # {'el': 'the', 'gato': 'cat', 'perro': 'dog', 'hola': 'hello'}
print(invert({"a": "x", "b": "x"}))                # {'x': 'b'}

print(group_by_length(["hi", "cat", "yo", "dog", "a"]))   # {2: ['hi', 'yo'], 3: ['cat', 'dog'], 1: ['a']}
print(group_by_length([]))                         # {}
