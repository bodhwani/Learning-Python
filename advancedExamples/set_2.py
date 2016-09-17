#Python that uses set and map

values = {10, 20, 30}

# Multiply all values in the set by 100.
result = map(lambda x: x * 100, values)

# Display our results.
for value in result:
    print(value)
"""
Output

1000
2000
3000
"""