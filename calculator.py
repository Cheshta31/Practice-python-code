def addition(a,b):
    sum=0
    sum=a+b
    return(sum)
def subtraction(a,b):
    diff=0
    diff=a-b
    return(diff)
def multiplication(a,b):
    mult=1
    mult=a*b
    return(mult)
def division(a,b):
    div=1
    div=a/b
    return(div)
def modulus(a,b):
    mod=a%b
    return(mod)
def square(a):
    sq=a*a
    return(sq)
def cube(a):
    cb=a*a*a
    return(cb)

def power(a,b):
    powe=a**b
    return(powe)
def operation():
    op=int(input("Enter operation to be performed:\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulus\n6.Power\n7.Square\n8.Cube"))
    if op==1:
        a,b=doubleinput()
        add=addition(a,b)
        print(a,"+",b,"=",add)
    if op==2:
        a,b=doubleinput()
        sub=subtraction(a,b)
        print(a,"-",b,"=",sub)
    if op==3:
        a,b=doubleinput()
        pro=multiplication(a,b)
        print(a,"*",b,"=",pro)
    if op==4:
        a,b=doubleinput()
        if b==0:
            print("Zero division error")
            bvalue()
        else:
            divi=division(a,b)
            print(a,"/",b,"=",divi)
    if op==5:
        a,b=doubleinput()
        if b==0:
            print("Zero division error")
            bvalue()
        else:
            modu=modulus(a,b)
            print(a,"%",b,"=",divi)
    if op==6:
        a,b=doubleinput()
        powe=power(a,b)
        print(a,"to the power",b,"=",powe)
    if op==7:
        a=singleinput()
        sq=square(a)
        print(a,"square is ",b,"=",sq)
    if op==8:
        a=singleinput()
        cb=cube(a)
        print(a,"cube is ",b,"=",cb)

def doubleinput():
    num=int(input("Which type of number do you want to enter \n1.integer\n2.float\n"))
    if num==1:
        a,b=int(input("Enter two no.")),int(input())
    elif num==2:
        a,b=float(input("Enter two no.")),int(input())
    else:
        print("Invalid choice")
        exit()
    return a,b
def singleinput():
    num=int(input("Which type of number do you want to enter \n1.integer\n2.float\n"))
    if num==1:
        a=int(input("Enter the no."))
    elif num==2:
        a=float(input("Enter the no."))
    else:
        print("Invalid choice")
        exit()
    return a
print("Welcome to Cheshta's Calculator")
operation()

    

