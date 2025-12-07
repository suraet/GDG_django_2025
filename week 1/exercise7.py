
def list(n):
 final_answer =  []
 for i in range(1,n + 1):
     if i%3 ==0 and i%5 == 0:
        final_answer.append("fizzbuzz")
     elif i%3 ==0:
        final_answer.append("fizz")
     elif i%5 == 0:
         final_answer.append("buzz")
     else:
        final_answer.append(str(i))

 return final_answer

n = int(input("enter the number "))
print(list(n))