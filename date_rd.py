import random
import time 
def name (p,f):
    print ('it will print a random date between,',p,'and',f)
    ai= random.random()
    dateformat = '%d-%m-%Y'
    g=time.mktime(time.strptime(p,dateformat))
    d=time.mktime(time.strptime(f,dateformat))
    rt =g + ai * (d -g )
    rd= time.strftime(dateformat, time. localtime(rt))
    return rd
print (name('1-01-1999','28-01-2028')) 
