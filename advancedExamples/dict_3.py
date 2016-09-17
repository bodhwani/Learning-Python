#Python that counts letter frequencies

# The first three letters are repeated.
letters = "abcabcdefghi"

frequencies = {}
for c in letters:
    # If no key exists, get returns the value 0.
    # ... We then add one to increase the frequency.
    # ... So we start at 1 and progress to 2 and then 3.
    frequencies[c] = frequencies.get(c, 0) + 1

for f in frequencies.items():
    # Print the tuple pair.
    print(f)

"""
Output

('a', 2)
('c', 2)
('b', 2)
('e', 1)
('d', 1)
('g', 1)
('f', 1)
('i', 1)
('h', 1)
"""