def num(r):
    e =len(r)  -1
    s=0
    while s < e:
        if r[s] != r[e]:
            return False
        s+=1
        e-=1
    return True
r=(1,2,3,2,1)

if (num(r)):
    print (r ,' is flip flop')
else:
    print (r ,' is not flip flop')