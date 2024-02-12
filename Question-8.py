"""8.Define a function that accepts 2 values and return its sum, subtraction and multiplication. Using 4 types of functions based on arguments and return type."""

# Define a function named 'calculation' which takes two arguments 'a' and 'b'
def calculation(a, b):
    # Calculate the sum, subtraction, and multiplication of 'a' and 'b'
    sum_result = a+b
    subtraction_result = a-b
    multiplication_result = a*b
    # Return the calculated results as a tuple
    return sum_result, subtraction_result, multiplication_result

# Get user input for 'a' and 'b'
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: ")) 

# Call the 'calculation' function with 'a' and 'b' and unpack the returned tuple into individual variables
sum_result, subtraction_result, multiplication_result = calculation(a, b)

print("Sum:",sum_result)
print("Subtraction: ", subtraction_result)
print("Multiplication: ", multiplication_result)