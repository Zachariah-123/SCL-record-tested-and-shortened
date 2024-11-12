def fact(num):
    prod = 1
    while True:
        if num==0:
            break
        prod *= num
        num -= 1
    return prod
    
num=int(input("Enter number:"))
print(fact(num))