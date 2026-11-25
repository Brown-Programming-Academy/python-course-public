# Created for: Introduction to Programming, Ariel University
# Homework 6 (optional)
# Topic: Recursion and Dictionaries
#
# Q1-Q3 are recursion questions. Q4-Q5 are dictionary questions
# (there is a short introduction to dictionaries right before Q4 - read it first).
# Every question is independent - run each block on its own.
#
# General rules for this homework:
#   - Functions should RETURN their answer - not print it!
#     (Printing is done outside the function, by the code that calls it.)
#   - In the recursion questions your solution must really be recursive.
#     In Q1 and Q2 don't use loops at all.
#     In Q3 you may use a for loop to go over the elements of ONE list,
#     but the "going deeper" must be done by recursion (like flatten from class).

############### Q1 ############
# Happy numbers 😊
# Take a positive number and replace it with the sum of the squares of its digits.
# Repeat. If we reach 1 - the number is HAPPY.
# If not, the numbers go around in a circle forever - the number is UNHAPPY.
#
#   19 is happy:    19 -> 1*1 + 9*9 = 82 -> 8*8 + 2*2 = 68 -> 6*6 + 8*8 = 100 -> 1*1 + 0*0 + 0*0 = 1
#   2 is unhappy:   2 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> ...
#                   (we are back at 4, and it will go on like this forever)
#
# a) Write a recursive function sum_square_digits(n) that RETURNS the sum of the squares of
#    the digits of n (n >= 0). Don't convert n to a string, and don't use loops.
#    Hint: the last digit of n is n % 10, and the rest of the number is n // 10.
#
# b) Write a recursive function is_happy(n) that RETURNS True if n is happy and False if not
#    (n >= 1). It should use sum_square_digits. Don't use loops.
#
#    Be careful: for an unhappy number the process never reaches 1, so a function that
#    just keeps calling itself would never stop (Python would stop it with a RecursionError).
#    How can we know that we are going around in a circle?
#    When we reach a number that we have ALREADY SEEN before.
#
#    So write a second function (a "helper") with an extra parameter - a list of the numbers
#    we have seen so far. The helper is the recursive one. It has TWO base cases:
#    reaching 1, and reaching a number that is already in the list.
#    The function is_happy(n) itself just calls the helper with an empty list.
#
# Examples:
#   sum_square_digits(19)   ->  82
#   sum_square_digits(123)  ->  14
#   sum_square_digits(7)    ->  49
#   sum_square_digits(0)    ->  0
#
#   is_happy(1)    ->  True
#   is_happy(7)    ->  True
#   is_happy(19)   ->  True
#   is_happy(100)  ->  True
#   is_happy(2)    ->  False
#   is_happy(4)    ->  False
#   is_happy(15)   ->  False
#
# Questions for thought (answer in a comment):
#   1) Try is_happy(2) with a version that has no list of seen numbers. What happens? Why?
#   2) For is_happy(19), what is the list of seen numbers at the moment the helper
#      reaches the number 1?

# Write your code here


############### Q2 ############
# Binary numbers 💻
# To write a number n in binary:
#   - the LAST binary digit is n % 2   (0 if n is even, 1 if n is odd)
#   - the rest of the digits are the binary form of n // 2
#
# Example: n = 13.   13 % 2 = 1, and 13 // 2 = 6, which is "110" in binary.  So 13 is "1101".
#
# a) Write a recursive function to_binary(n) that RETURNS the binary form of n (n >= 0)
#    as a STRING. Don't use bin() or format(), and don't use loops.
#
# b) Write a recursive function count_ones(n) that RETURNS how many 1s there are in the
#    binary form of n (n >= 0). Don't convert n to a string, don't use to_binary, and don't use loops.
#    Hint: use only n % 2 and n // 2.
#
# Examples:
#   to_binary(0)     ->  "0"
#   to_binary(1)     ->  "1"
#   to_binary(10)    ->  "1010"
#   to_binary(13)    ->  "1101"
#   to_binary(255)   ->  "11111111"
#
#   count_ones(0)    ->  0
#   count_ones(8)    ->  1
#   count_ones(13)   ->  3
#   count_ones(255)  ->  8
#
# Questions for thought (answer in a comment):
#   1) What is the base case of to_binary?
#   2) In to_binary, the last digit is written AFTER the result of the recursive call.
#      What would to_binary(10) return if you wrote it BEFORE the recursive call? Try it, and explain.

# Write your code here


############### Q3 ############
# Boxes inside boxes 📦
# A box is a list. Inside a box there can be numbers (coins) and other boxes,
# and those boxes can have more boxes inside them, at any depth.
#
#     [1, [2, 3], [4, [5]]]
#
# This box has one coin on its own level (the 1), a box [2, 3] with two coins,
# and a box [4, [5]] which has one more box [5] inside it.
#
# a) Write a recursive function sum_nested(box) that RETURNS the sum of ALL the numbers
#    in the box, at every depth.
#
# b) Write a recursive function count_boxes(box) that RETURNS how many boxes (lists) there are
#    in total - the box itself, and every box inside it, at every depth.
#
# Hint: to check if an element is a box use  isinstance(item, list)
#       (it does the same as  type(item) == list)
#
# Examples:
#   sum_nested([1, [2, 3], [4, [5]]])    ->  15
#   sum_nested([10, [20, [30]]])         ->  60
#   sum_nested([])                       ->  0
#   sum_nested([[], [[]]])               ->  0
#
#   count_boxes([1, [2, 3], [4, [5]]])   ->  4      (the big box, [2, 3], [4, [5]] and [5])
#   count_boxes([1, 2, 3])               ->  1      (just the box itself)
#   count_boxes([])                      ->  1
#   count_boxes([[], [[]]])              ->  4
#
# Questions for thought (answer in a comment):
#   1) What does sum_nested return for an empty box? Do you need a special "if" for it?
#   2) In count_boxes, why do we start counting from 1 and not from 0?

# Write your code here


############### Dictionaries - a short introduction (read before Q4 and Q5) ############
# A list keeps its values by POSITION: 0, 1, 2, ...
# A dictionary keeps its values by a KEY that we choose - a name, a word, any number.
# Like a phone book: we look up the NAME and get the number.
# Every entry in a dictionary is a pair   key: value
#
#   Create:     ages = {"Dana": 20, "Omer": 22, "Noa": 19}
#   Empty one:  empty = {}
#
#   Look up:    ages["Noa"]              ->  19
#               ages["Lior"]             ->  KeyError  (there is no key "Lior" - the program crashes)
#
#   Add/change: ages["Lior"] = 21        a NEW key - adds an entry
#               ages["Omer"] = 23        an EXISTING key - changes its value
#               (the same syntax does both)
#
#   Delete:     del ages["Dana"]         removes the entry
#
#   Check:      "Noa" in ages            ->  True   (in checks the KEYS - not the values)
#               19 in ages               ->  False
#
#   Safe look up:   ages.get("Lior", 0)  ->  the value of "Lior", or 0 if there is no such key
#                   ages.get("Lior")     ->  the value, or None if there is no such key
#
#   Size:       len(ages)                ->  the number of entries
#
# Going over a dictionary:
#   for name in ages:                    # a for loop over a dictionary gives the KEYS
#       print(name, ages[name])          # and with a key we can get its value
#
#   for name, age in ages.items():       # or both the key and the value together
#       print(name, age)
#
#   ages.keys()      -> all the keys        ages.values()  -> all the values
#   (use list(ages.keys()) if you want to see them as a list)
#
# Rules:
#   - Keys are unique. Writing to an existing key replaces the old value.
#   - Keys must be of an immutable type (str, int, tuple...). A list can't be a key.
#   - Values can be anything - numbers, strings, even lists. For example:
#         scores = {"Dana": [90, 85]}
#         scores["Dana"].append(70)      # the value is a list, so we can change it
#         print(scores)                  # {'Dana': [90, 85, 70]}
#
# Try it! Copy these lines, run them, and change them to see what happens:
#
#   ages = {"Dana": 20, "Omer": 22, "Noa": 19}
#   ages["Lior"] = 21
#   ages["Omer"] = 23
#   print(ages)                          # {'Dana': 20, 'Omer': 23, 'Noa': 19, 'Lior': 21}
#   print("Noa" in ages, 19 in ages)     # True False
#   print(ages.get("Yossi", 0))          # 0
#   for name in ages:
#       print(name, "is", ages[name])


############### Q4 ############
# A small shop 🛒
# A shop keeps its prices in a dictionary: the key is the name of a product,
# and the value is its price.
#
# a) Write a short program (no function) that does the following, in this order:
#    1) create the dictionary  prices  with:  apple: 3,  banana: 2,  milk: 7
#    2) print the price of milk
#    3) add a new product: bread, which costs 5
#    4) change the price of apple to 4
#    5) print whether "cheese" is sold in the shop (True/False)
#    6) delete banana from the shop
#    7) print how many products there are now
#    8) go over all the products with a for loop and print every one like this:  apple costs 4
#
#    The output should be:
#       7
#       False
#       3
#       apple costs 4
#       milk costs 7
#       bread costs 5
#
# b) Write a function total_cost(prices, basket) that gets the prices dictionary and a list of
#    product names (the basket), and RETURNS the total price of the basket.
#    The same product can appear more than once in the basket.
#    A product that is not sold in the shop costs 0.
#    Hint: use get.
#
# c) Write a function expensive_items(prices, limit) that RETURNS a list of the names of
#    the products whose price is HIGHER than limit.
#
# Examples (for the original prices - apple: 3, banana: 2, milk: 7):
#   total_cost(prices, ["apple", "milk", "apple"])   ->  13
#   total_cost(prices, ["bread", "milk"])            ->  7       (the shop doesn't sell bread)
#   total_cost(prices, [])                           ->  0
#   expensive_items(prices, 2)                       ->  ['apple', 'milk']
#   expensive_items(prices, 10)                      ->  []
#
# Questions for thought (answer in a comment):
#   1) What happens if you write prices["cheese"] for a product that is not in the shop?
#      How did you avoid this in total_cost?
#   2) In part (c), what do you get when you go over the dictionary with  for name in prices ?
#      How did you get the price?

# Write your code here


############### Q5 ############
# Translator 🌍
# A dictionary is a natural way to keep a translation: the key is a word in English,
# and the value is the same word in Spanish.
#
#     words = {"the": "el", "cat": "gato", "dog": "perro", "hello": "hola"}
#
# a) Write a function translate(sentence, words) that gets a sentence (words separated by spaces,
#    all in lower case) and RETURNS the sentence with every word that is in the dictionary
#    translated. Words that are not in the dictionary stay as they are.
#    Hint: split the sentence, build a new list of words (use get!), and join it back with " ".join.
#
# b) Write a function invert(words) that RETURNS a NEW dictionary in which the keys and the
#    values are swapped (so we can translate back from Spanish to English).
#    Assume that all the values are different from each other.
#
# c) Challenge: write a function group_by_length(words) that gets a list of words and RETURNS
#    a dictionary: the key is a length, and the value is a LIST of all the words of that length,
#    in their original order.
#
# Examples:
#   translate("the cat and the dog", words)   ->  "el gato and el perro"
#   translate("hello", words)                 ->  "hola"
#   translate("good morning", words)          ->  "good morning"
#
#   invert(words)   ->  {'el': 'the', 'gato': 'cat', 'perro': 'dog', 'hola': 'hello'}
#
#   group_by_length(["hi", "cat", "yo", "dog", "a"])   ->  {2: ['hi', 'yo'], 3: ['cat', 'dog'], 1: ['a']}
#   group_by_length([])                                ->  {}
#
# Questions for thought (answer in a comment):
#   1) In translate, why is  words.get(word, word)  a good choice? What does the second "word" do?
#   2) What happens in invert if two English words have the same Spanish translation?
#      For example: {"a": "x", "b": "x"}

# Write your code here
