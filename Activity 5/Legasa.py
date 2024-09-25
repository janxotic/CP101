import string

def count_characters(text):

  lowercase_count = 0
  uppercase_count = 0
  digit_count = 0
  special_symbol_count = 0

  for char in text:
    if char.islower():
      lowercase_count += 1
    elif char.isupper():
      uppercase_count += 1
    elif char.isdigit():
      digit_count += 1
    else:
      special_symbol_count += 1

  return {
      'lowercase': lowercase_count,
      'uppercase': uppercase_count,
      'digits': digit_count,
      'special_symbols': special_symbol_count
  }

# Get user input
text = input("Enter a string: ")

# Count characters
result = count_characters(text)

# Print the result
print(result)
