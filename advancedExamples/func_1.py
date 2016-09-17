#Python program that uses recursion

def recursive(depth):
    # Stop recursion if depth exceeds 10.
    if depth > 10:
        return

    print(depth)

    # Call itself.
    recursive(depth + 1)

# Begin.
recursive(5)
"""
Output

5
6
7
8
9
10
"""