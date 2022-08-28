from collections import Counter
a=[2,3,4,3,2,4]
words=['cat','dog','cat','dog']
print(Counter(a))
print(Counter(words))

countw=Counter(words)
countw['cat']=100
print(countw)
for i in countw:
    print(i)
    if i=='cat':
        print("in")
        countw['cat']=400

                
print(countw) 