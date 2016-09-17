# Reversing digits of a number
n=123456789
rev=0
while (n>0):
   rev = rev*10 + n%10
   n/=10
print rev
