ie=int(input("Longer Diameter of Diamond:\t"))
if ie % 2 == 0:
    pass
else:
    ie += 1
ei=int(ie/2)
s=' '
p='*'
for i in range(1,ie):
    j=ie-i
    if(i<ei):
        print(s*(ei-i),p*(2*i-1))
    else:
        print(s*(ei-j),p*(2*j-1))
#