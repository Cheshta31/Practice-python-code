#user defined program for calculation even or odd no.
a=float(input('Plz enter a no.'))
print(type(a))
b=a%2
print(b)
if(a==0):
    print("Neither even nor odd")
elif(a%2==0):
    print("Even")
else:
    print("Odd")
    
