#Python that receives tuple argument

def display(*t):
    # Print tuple.
    print(t)

    # Loop over tuple items.
    for item in t:
        print(item)

# Pass parameters.
display("San Francisco", "Los Angeles", "Sacramento")
display(2, 0, 1, 4)

'''Output

('San Francisco', 'Los Angeles', 'Sacramento')
San Francisco
Los Angeles
Sacramento
(2, 0, 1, 4)
2
0
1
4
'''
