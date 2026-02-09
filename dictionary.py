dj={'Id1': {'Name':'Anas','Age':12,'Grade':'6A'},
'Id2':{'Name':'Devanshi','Age':14,'Grade':'8A'},
'Id3':{'Name':'python','Age':200,'Grade':'out of school'},
    'Id4':{'Name':'Nartou','Age':15,'Grade':'9A'}}
resalt={}
for Key,Value in dj.items():
    if Value not in resalt.values():
        resalt[Key]=Value


print(resalt)