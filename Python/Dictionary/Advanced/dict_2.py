#Python that uses fromkeys

# A list of keys.
keys = ["bird", "plant", "fish"]

# Create dictionary from keys.
d = dict.fromkeys(keys, 5)

# Display.
print(d)
"""
Output

{'plant': 5, 'bird': 5, 'fish': 5}
"""