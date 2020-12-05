course = 'Python for Beginners'
print(course)

print(course[0])

print(course[-1]) # refers to the character from the end
print(course[-2])

print(course[0:3])

# Formatted String

first = 'Jibin'
last = 'Reji'
message = first + ' [' + last + '] is a coder!'  # String Concatenation
# This makes confusion bcs its not formatted
print(message)

"we use 'f' and '{} called as PLACE HOLDER' to format a long string"

msg = f'{first} [{last}] is a coder!'

print(msg)
