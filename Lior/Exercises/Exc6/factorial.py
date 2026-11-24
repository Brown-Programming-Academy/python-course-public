def factorial(x):
    if x == 0:
        return 1
    
    return (factorial(x-1) * x)

# Main loop
x = int(input("insert non-negative integer"))

if x >= 0:
    print(factorial(x))
else:
    print("WASSAP BOZO, this is negative")