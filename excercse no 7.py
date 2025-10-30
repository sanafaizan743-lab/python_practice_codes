def divisibleby5(numberlist):
    for number in numberlist:
        if number % 5 == 0:
            print(number)
        else:
            continue
numbers=[10,20,34,56,78]
divisibleby5(numbers)