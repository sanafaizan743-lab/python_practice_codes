char=input("enter the string ")
index=0
for index in range(len(char)):
    if(index % 2 == 0):
        print(char[index])
    else:
        print("")
