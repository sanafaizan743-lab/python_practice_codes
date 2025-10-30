def multiplication_or_sum(num1, num2):
    # calculate product of two number
    product = num1*num2
    # check if product is less then 1000
    if product <= 1000:
        return product
    else:
        # product is greater than 1000 calculate sum
        return num1+num2

