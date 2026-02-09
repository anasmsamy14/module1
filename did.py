did={"codingal":2,"is":2,"better":2,"than":2,"ischool":2}
print('og dictionary is',did)
codin=2
count= 0
for key in did:
    if did[key]==codin:
        print(key)
        count += 1
print("The value", codin, "appears", count, "times in the dictionary.")