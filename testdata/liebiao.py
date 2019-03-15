a=[i for i in range(10) if i%2==0]
print(a)
b=[11,22,33,11,22,33]
c=[]
for i in b:
    if i not in c:
        b.append(i)
#去重