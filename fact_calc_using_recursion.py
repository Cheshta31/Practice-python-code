#factorial calculation using recursion

def fact(x):
    y=1
    if x==0 or x==1:
        return y
    else:
        y=x*fact(x-1)
        return y
x=int(input("Enter a no. = "))
y=fact(x)
print("Factorial = ",y)
