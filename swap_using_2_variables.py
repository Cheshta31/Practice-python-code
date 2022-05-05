#swap without using 3rd variable
print("In this python script,values are swapped without using 3rd variable")
x=int(input("Enter a no. = "))
y=int(input("Enter another no. = "))
print("Values before swapping")
print("First =",x)
print("Second =",y)
x=x+y
y=x-y
x=x-y
print("After swapping")
print("First no. = ",x)
print("Second no. = ",y)
