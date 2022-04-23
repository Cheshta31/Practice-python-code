#string reversal using swapping
print("To reverse a string using swapping")
a=input("Plz enter a string")
x=len(a)
print("String after reversal = ")
str1=""
for i in range (x-1,-1,-1):
    str1+=a[i]
print(str1)
#string reversal without using swapping
print("String reversal without doing swapping")
str1=input("Enter a string")[::-1]
print("Reversed string = ",str1)

    
