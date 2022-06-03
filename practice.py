class Person:
    def __init__(self, name):
        self.name=name
        
        
p = Person("Saido")
print(p.name)
        


# create an object by calling the class

   














































# def leap_year(year):
#     if year%4==0 or year%400==0:
#         print("True")
#     elif year%100 !=0:
#         print("True")

#     else:
#         print("false")


# leap_year(2014)


# def numbers():
#     for num in range(1,20):
#         if num%2==0:
#             print("Fizz")
#         elif num%3==0:
#             print("Buzz")
#         elif num%3==0 or num%6==0:
#             print("fizz Buzz")

#         else:
#             print(num)

# numbers()


# def divisible_by_three(n):
#     for num in range(1,n):
#         if num%3==0:
#             print(num)

# divisible_by_three(20)


# num = int(input("Enter your number:"))
# if (num%2) == 0:
#     print("{0} is Even number".format(num))
# else:
#     print("{0} is Odd number".format(num))


# num1 = 10
# num2 =12
# num3 = 14

# if(num1>=num2) and (num1>=num3):
#     largest=num1
# elif(num2>=num1) and (num2>=num3):
#     largest= num2
# else:
#     largest=num3

# print("largest number is ", largest)

# from math import factorial


# num=7
# factorial=1
# if num<0:
#     print("factorial is not")
# elif num == 0:
#     print("factorial 0 is 1")
# else:
#     for i in range(1,num +1):
#         factorial=factorial*i
#     print("the factorial", num, "is", factorial)

# def factorial(n):
     
    # single line to find factorial
#     return 1 if (n==1 or n==0) else n * factorial(n - 1);

# num = 5;
# print("Factorial of",num,"is",
# factorial(num))