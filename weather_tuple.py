
weather = (1,0,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,)
sunny =0
rainy = 0
for i in range (len(weather)):
    if weather[i]==1:
        rainy +=1
    else:
        sunny +=1
if sunny > rainy:
    print ('hot weather')
else:
    print ('rainy weather')