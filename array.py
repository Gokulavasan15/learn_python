from array import *
vals = array('i',[5,6,8,8,9])
newarr = array(vals.typecode,(a*2 for a in vals ))
for a in newarr:
    print(a)