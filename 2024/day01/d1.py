l1=[]
l2=[]
with open('input.txt', 'r') as file:
    for line in file:
        l=line.split()
        l1.append(int(l[0]))
        l2.append(int(l[1]))


l1.sort()
l2.sort()

l1t=list(tuple(l1))
l2t=list(tuple(l2))

sum=0
for i in range(0,len(l1t)):
    sum+=abs(l1t[i]-l2t[i])

print(sum)

f={}

for i in l1t:
    f.setdefault(i,0)

for i in l2:
    if i in f:
        f[i]+=1

sum=0
for i in f.items():
    sum+=i[0]*i[1]

print(sum)