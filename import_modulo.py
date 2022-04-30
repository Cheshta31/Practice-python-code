#1st method
print("1st method for importing square root module")
import math
x=4
y=math.sqrt(x)
print(x)
print(y)

#2nd method
print("2nd method for importing square root module")
import math as m
x=4
y=m.sqrt(x)
print(x)
print(y)
#for importing only selected functions from a library
print("Method for only importing selected functions(square root) from math library")
from math import sqrt
x=4
y=math.sqrt(x)
print(x)
print(y)
