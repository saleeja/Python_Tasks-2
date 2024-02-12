"""6.Write a Python function that takes a number as a parameter and checks whether the number is prime or not"""


# A prime number is defined as a natural number greater than 1 and is divisible by only 1 and itself. 


def prime(number):
# prime number is always greater than 1
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                print(number, "is not a prime number")
               
        else:
            print(number, "is a prime number")

    else:
        print(number, "is not a prime number")


prime(2)