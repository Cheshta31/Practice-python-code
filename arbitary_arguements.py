def avg(*value):
    x=0
    for i in value:
        x=x+i
    return x/len(value)
y=avg(3,4,5)
print(y)
#user defined program for arbitary arguements
print("User defined arbitary arguements")
def avg(*value):
    x=0
    for i in value:
        x=x+i
    return x/len(value)
a=int(input("Enter 1st no. "))
b=int(input("Enter 2nd no. "))
c=int(input("Enter 3rd no. "))
y=avg(a,b,c)
print(y)
