from multiprocessing.connection import answer_challenge


def multiply_or_sum(num1,num2):
   product = num1 * num2
   sum = num1 + num2
   if product <= 1000:
      return product
   else:
      return sum

num1 = int(input("enter the number "))
num2 = int(input("enter the number "))
result = multiply_or_sum(num1,num2)
print("the result is " ,result)