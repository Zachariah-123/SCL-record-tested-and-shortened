def fib():
    num=int(input("Enter number of characters :"))
    flag = 0 
    prev = 0
    present = 1
    l=[]
    while True:
        next=prev+present
        prev=present
        present=next
        l.append(prev)
        flag+=1
        if flag == num:
            break
    return l
print(fib())