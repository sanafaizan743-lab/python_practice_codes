def removeletters(sentence,n):
    result=""
    for index in range(n,len(sentence)):
        result+=sentence[index]
    return result

word= input("enter word :")
sentence=removeletters(word,3)

print(sentence)
