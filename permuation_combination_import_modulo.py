import recursion as r

        
x=int(input("Enter total values = "))
y=int(input("Enter any value = "))
fx=r.fact(x)
fy=r.fact(x-y)
p=fx/fy
print("Permuation = ",p)
