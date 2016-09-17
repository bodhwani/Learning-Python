# Printing pattern
n=5
for i in range (1,n+1):
    for j in range (i,n):
        print "",
    for j in range (1,i+1):
        print j,
    print '\n'

