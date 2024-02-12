# 3.Write a Python function to find the maximum of three numbers.

def find_maximum(num1, num2, num3):
    return max(num1, num2, num3)

num1 = int(input("Enter a number:"))
num2 = int(input("Enter a number:"))
num3 = int(input("Enter a number:"))

maximum_value = find_maximum(num1, num2, num3)
print(f"The maximum number is: {maximum_value}")
