a=[4,6,7,8,11]
#erase first element array
length=len(a)
for i in range(0,length-1):
    a[i]=a[i+1]
print(a)
a=[4,6,7,8,11]
# erase element in an specific position
# delete 7
print(a)
position_delete=2
for i in range(position_delete,length-1,1):
    a[i]=a[i+1]
print(a)

