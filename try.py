try:
    x=int(input("enter a number: "))
    print (2/x)
except ValueError as ex:
    print("exception", ex)n