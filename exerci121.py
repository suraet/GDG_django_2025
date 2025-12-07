def squrt (x:int)->int:
    if x <2:
        return x 
    low = 1 
    high = x
    result =0
    while low <= high : 
        mid = low +(high - low)//2
        midsqur = mid*mid
        if midsqur == x :
            return mid 
        elif midsqur<x :
            result=mid
            low=mid+1 
        else :
            high = mid-1
    return result
a= squrt(int(input("enter the number")))
print(a)