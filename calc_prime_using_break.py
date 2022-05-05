#calculate prime no. using break statement
n=int(input("Enter a no. "))
count=0
for i in range (2,n-1):
    if(n%i==0):
        print("Not a prime no.")
        break
    else:
        print("prime no.")
        break
