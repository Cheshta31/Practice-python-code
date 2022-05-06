str1="The fish is in the pond"
x=len(str1)
#print("length of string 1 is",x)
print("Length of str1 = "+str(x))
#for i in range(x):
    #print("{} is at index {}".format(str1[i],i))
'''y=str1.index("I")   
print("Index of I character",y)
'''
'''for i in str1:
    print(i,"is at index",str1.index(i))'''
for i in range(x-1,-1,-1):
    print(str1[i])
