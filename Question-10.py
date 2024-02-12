"""10.Define a function that accepts lowercase words and returns uppercase words."""


def convert_to_uppercase(words):
    uppercase_words = words.upper()
    return uppercase_words


lowercase_input = "hello world"
result = convert_to_uppercase(lowercase_input)
print("Uppercase:",result)
