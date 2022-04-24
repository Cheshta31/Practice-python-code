def even(n):
    return n%2==0
def odd(n):
    return n%2!=0
list1=[23,67,22,34,78,11,56,42]
list_even=list(filter(even,list1))
list_odd=list(filter(odd,list1))
print("List of no. = ",list1)
print("List of even no. = ",list_even)
print("List of odd no. = ",list_odd)


