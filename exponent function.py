def exponentfunction(base_num,pow):
    result=1
    for i in range(0,pow):
        result=base_num*result
    return result
number=int(input("enter the number : "))
power=int(input("enter the power: "))
answer=exponentfunction(number,power)
print(answer)

