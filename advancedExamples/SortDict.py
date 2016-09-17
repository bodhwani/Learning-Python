import operator
x = {'a':5,'b':4,'c':3,'d':2,'e':1}
print "Dictionary",x # data in dictionary is stored in random order
sortValues = sorted(x.items(), key=operator.itemgetter(1))
print "Sorted data by value",sortValues
sortKeys = sorted(x.items(), key=operator.itemgetter(0))
print "Sorted data by key",sortKeys
