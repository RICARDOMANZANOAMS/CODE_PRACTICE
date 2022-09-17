#insert at the beginning
a=[12,24,33,47,58]
size=len(a)
for idx in range(size-1,-1,-1):
    a[idx]=a[idx-1]
a[0]=20
print(a)

#insert at the middle
#between 24 and 33
a=[12,24,33,47,58]
print("original")
print(a)
position_to_insert=2
for idx in range(size-1,position_to_insert,-1):
    a[idx]=a[idx-1]
a[2]=55
print("insert middel")
print(a)
