"""1.Write a Python function that calculates the factorial of a given integer. Demonstrate how to call this function with an example."""

def factorial(number):
# factorial of 1 and 0 is 1
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)

# Calculate factorial
number = int(input("Enter a number:"))
result = factorial(number)
print("The factorial is:",result)
