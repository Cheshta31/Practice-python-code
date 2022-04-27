t1=(2,4,6,8,20)
t2=(9,5,3,12,88)
print(t1)
print(id(t1))
t1+=t2
print(t1)
print(id(t1))
#id of t1 changes because memory location change after performing an
#operators in case of tuple but in case of list the memory location
#remains the same and so id does not change
