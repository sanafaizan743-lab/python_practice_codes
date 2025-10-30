number=[1, 2, 3, 4,5 ,6 ,7 ,8 ,9, 10]
index=0
result=0
for index in range(len(number)):
    result = result + number[index]
    index=index+1

print("the result is " ,result)