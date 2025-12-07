# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mult(a,b):
#     return a*b
# def div(a,b):
#     return a/b
# a= int(input("wnter the first number "))
# o=input("enter the operator ")
# b= int(input("enter the second number"))
# if o =="+":
#     print(add(a,b))
# elif o =="-":
#     print(sub(a,b))
# elif o=="*":
#     print(mult(a,b))
# else :
#     if b==0:
#         print("error ")
#     else:
#         print(div(a,b))
ex = input("wnter the expression ")
try:
    result = eval(ex)
    print(result)
except:
    print("invalid ")