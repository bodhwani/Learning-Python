# Print count of each character in  string

s="This is ACM workshop on python"
d=dict()
for i in s:
    if(d.has_key(i)):
        d[i] += 1
    else:
        d[i]=1

del d[' ']
print d

