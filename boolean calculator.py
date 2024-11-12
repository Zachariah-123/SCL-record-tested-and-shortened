def boolnot(a):
    return not a


def booland(a,b):
    return (a and b)


def boolor(a,b):
    return (a or b)


def boolxor(a,b):
    return(a ^ b)

while True: 
    op = input("and , or , not ,xor:")
    a = bool(input("Enter a:"))
    b= bool(input("Enter b:"))
    
    match op:
        case "and":
            print(booland(a,b))
        case "or":
            print(boolor(a,b))
        case "not":
            print(boolnot(a))
            print(boolnot(b))
        case "xor":
            print(boolxor(a,b))
        case _:
            print("Invalid Entry ending sequence")
            break
input()