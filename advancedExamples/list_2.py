list = [10, 20, 30]

# Use "v" identifier to refer to the list.
# ... Access its elements in format.
res = str.format("The values are {v[0]}, {v[1]} and {v[2]}", v=list)
print(res)

"""
Output

True
False
"""