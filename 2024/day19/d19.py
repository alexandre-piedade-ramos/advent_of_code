filename="input.txt"
with open(filename,'r') as file:
    filetext=file.readlines()
    towels=filetext[0].split(',')
    patterns=filetext[2:]
    towels=[e.strip() for e in towels]
    patterns=[e.strip() for e in patterns]

towels.sort(key=lambda e: (e,len(e)))
mem=[[0 if j>0 else 1 for j in range(len(p)+1)] for p in patterns]

for i in range(len(patterns)):
    p=patterns[i]
    for j in range(0,len(p)):
        if mem[i][j]==0:
            continue
        for t in towels:
            if t[0]>p[j]:
                break
            if p[j:j+len(t)]==t:
                mem[i][j+len(t)]+=mem[i][j]
    print(p,mem[i][-1])

count1=0
count2=0
for e in mem:
    if e[-1]>0:
        count1+=1
    count2+=e[-1]
print(count1,count2)
