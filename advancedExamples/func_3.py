#Python that receives dictionary argument

def display(**values):
    # Loop over dictionary.
    for key in values:
        print(key, "=", values[key])

    # Newline.
    print()

# Pass named parameters.
display(first = "Sigmund", last = "Freud", year = 1899)
display(one = 1, two = 2)
"""
Output

year = 1899
last = Freud
first = Sigmund

two = 2
one = 1
"""