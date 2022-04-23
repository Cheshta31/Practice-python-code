a,b,c=int(input("Enter a no.")),int(input("Enter two no.")),int(input("Enter three no."))
if(a==b==c):
    print("All values are equal")
elif(a==b) and(a>c) and(b>c):
    print(a,"and",b,"are equal but greater than",c)
elif(a==c) and(a>b) and(c>b):
    print(a,"and",c,"are equal but greater than",b)
elif(b==c) and(b>a) and(c>a):
    print(b,"and",c,"are equal but greater than",a)
elif(a==b) and(a<c) and(b<c):
    print(a,"and",b,"are equal but less than",c)
elif(a==c) and(a<b) and(c<b):
    print(a,"and",c,"are equal but less than",b)
elif(b==c) and(b<a) and(c<a):
    print(b,"and",c,"are equal but less than",a)
elif(a>b) and (a>c):
    print(a,"is greater than",b,"and",c)
elif(b>a) and (b>c):
    print(b, "is greater than",a,"and",c)
else:
    print(c,"is greater than",b,"and",c)
