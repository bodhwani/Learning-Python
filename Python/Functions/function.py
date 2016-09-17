#function
def myfunc():
    print "You are in my function"
myfunc()

#function with argument
def func1(x,y):
    s=x+y
    print "sum of numbers is- ",s
func1(5,10)

#function with default parameter
def func2(first="Deepika",second="Katrina"):
    print "%s and %s are good friends "%(first,second)

func2("Vibhore","Vinit")
func2("Vibhore")
func2(second="Vibhore")

#function with return without argument
def func3():
    a=10
    b=20
    return a*b
p=func3()
print p

#function with return statements
def add_sum(x,y):
    return x+y

total=add_sum(x,y)
print total

#recursive(pres ctrl+c to stop)
def recurse():
    print "I will repeat"
    recurse()
recurse()




