def get_expensive_product(price):
        for p in price: #chek every element in the list 
            if p > 100 :
             print(p) 
price = [120,45,300,85,150]
a = get_expensive_product(price)
print(a)