ask= str(input('enter a word: ' ))
ans= str(input("enter a charchter from that word: "))
i=0
count = 0
while i < len(ask):
    if(ask [i] == ans):
        count = count+1 
    i = i+1
print(ans, "is repeted", count,"times")