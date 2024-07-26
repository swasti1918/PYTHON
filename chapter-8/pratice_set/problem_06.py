def cms():
    a = int(input("Enter a number"))
    b = a * 2.54
    print(b)  
    
cms()

## Another method

def inch_to_cms(inch):
    return inch * 2.54

n = int(input("Enter value in inches: "))

print(f"The corresponding value in cms is {inch_to_cms(n)}")