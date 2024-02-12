"""7.Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
Sample Items : green-red-yellow-black-white
Expected Result : black-green-red-white-yellow"""

def sort_sequence(sequence):
    # Split the input sequence into a list of words
    words = sequence.split('-')

    # Sort the list of words alphabetically
    sorted_words = sorted(words)

    # Join the sorted words into a hyphen-separated sequence
    result_sequence = '-'.join(sorted_words)

    return result_sequence

input_sequence = input("Enter a hyphen-separated sequence of words: ")
sorted_sequence = sort_sequence(input_sequence)
print("Sorted Result:", sorted_sequence)
