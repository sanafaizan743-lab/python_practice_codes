k=4
l=1
for i in range(0,10):
    if i>=5:
        for j in range(k,0,-1):
            print("*",end="  ")
        k=k-1
    else:
        for j in range(0,l):
            print("*",end="  ")
        l=l+1
    print()


