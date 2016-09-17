#Python that uses tuples as dictionary keys

# A tuple with two numbers.
pair = (1, 2)

# Create a dictionary.
# ... Use the tuple as a key.
dict = {}
dict[pair] = "Python"

# Access the dictionary using a tuple.
print(dict[(1, 2)])
"""
Output

Python
"""