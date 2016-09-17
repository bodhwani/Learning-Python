def lastchar(s):
    # Return last character in string.
    return s[-1]

# Input.
values = ["abc", "bca", "cab"]

# Sort by last character in the strings.
values.sort(key=lastchar)
print(values)

# Sort by the second character in the strings.
# ... Use a lambda expression.
values.sort(key=lambda s: s[1])
print(values)

"""
Output

['bca', 'cab', 'abc']
['cab', 'abc', 'bca']
"""