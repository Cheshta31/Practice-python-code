#calculate prime no. using for else break statement
n=int(input("Enter a no."))
for i in range(2,n-1):
      if(n%i==0):
          print("Not Prime no.")
          break
else:
    print("prime no.")



