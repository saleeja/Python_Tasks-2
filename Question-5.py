'''5.Write a Python function that accepts a string and counts the number of upper and lower case letters.'''

def count_letters(letter):
    upper_count = 0
    lower_count = 0

    for char in letter:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count

letter = input("Enter a letter:")

upper_count, lower_count = count_letters(letter)

print(f"Number of Upper Case Letters: {upper_count}")
print(f"Number of Lower Case Letters: {lower_count}")
