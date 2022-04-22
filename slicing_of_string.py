#Not a user defined program
a="Hello my name is Cheshta"
print(a)
x=len(a)
print("Length  of string = ",x)
b=a[5:24]
print("String after slicing = ",b)
#user defined program
str1=input("Enter a string")
print(str1)
x,y=int(input("Enter index to begin slicing")),int(input("Enter index to end slicing"))
str2=str1[x:y]
print("String after slicing",str2)
