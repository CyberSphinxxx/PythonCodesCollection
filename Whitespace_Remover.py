# This function takes an input string and uses the strip() method to remove
# leading and trailing whitespaces from it. Then, it returns the modified string.
def remove_whitespace(input_string):
    return input_string.strip()

# Example usage:

# Define a string with leading and trailing whitespaces
input_string = "   Hello, world!   "

# Call the remove_whitespace function with the input string
# and store the result in the 'result' variable
result = remove_whitespace(input_string)

# Print the original string with leading and trailing whitespaces
print("Original string:", input_string)

# Print the modified string with leading and trailing whitespaces removed
print("String with leading and trailing whitespaces removed:", result)
