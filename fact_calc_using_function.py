#factorial calculation using function

def fact(x):
    y=1
    if x==1 or x==0:
        return y
    else:
        for i in range(x,0,-1):
            y=y*i
        return y
x=int(input("Enter any no. = "))
y=fact(x)
print("Factorial of any no. = ",y)
