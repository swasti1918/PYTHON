def greater():
    a = int(input("Enter your number:"))
    b = int(input("Enter your number:"))
    c = int(input("Enter your number:"))
    
    if(a>b and a>c):
        print("A is greater")
    if(b>a and b>c):
        print("B is greater")
    if(c>a and c>b):
        print("C is greater")
        
greater()


## Another method

def greatest(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>b and c>a):
        return c

a = 1
b = 23
c = 3

print(greatest(a, b, c))
                


