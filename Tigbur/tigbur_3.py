# program that checks a new password option if it holds the criteria.
# no spaces
# atleast 8 chars
# has an uppercase
# has a digit
# has a lowercase

def no_spaces(p):
    if " " in p:
        return False
    return True

def is_long(p):
    if len(p) < 8:
        return False
    return True

def has_upper(p): # p = hellonoam
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for ltr in p:
        if ltr in upper_case:
            return True
    return False

def has_lower(p):
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    for ltr in p:
        if ltr in lower_case:
            return True
    return False

def has_digit(p):
    digits = "0123456789"
    for ltr in p:
        if ltr in digits:
            return True
    return False

def is_valid(p):
    valid = True
    if is_long(p) == False:
        print("too short")
        valid = False
    if no_spaces(p) == False:
        print("no spaces allowed")
        valid = False
    if has_lower(p) == False:
        print("needs lowercase")
        valid = False
    if has_upper(p) == False:
        print("needs upper")
        valid = False
    if has_digit(p) == False:
        print("needs digit")
        valid = False

    if valid == True:
        print("password accepted")
        return True
    print("try again")
    return False

# main
pswd = input("Enter Password: ")
while is_valid(pswd) == False:
    pswd = input("Enter Password: ")

    