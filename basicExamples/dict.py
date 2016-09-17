#dictionary creation
d={'RANBIR':'katrina','VIRAT':'anushka','RANVEER':'deepika'}
d['RANBIR']='katrina'

#displaying keys
d.keys()
list(d.keys())

#
for v in d.items():
    print v

#
for k in d.keys():
    print k
#
for k in d.keys():
    print k,d[k]

#
for k,v in d.items():
    print k,v

#
sorted(d.keys())

#
sorted(d.values())

#other method to create dict
g=dict([('vibhore','bimaar'),('harshit','sanki'),('vinit','slow')])

#

    
