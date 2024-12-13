def defective(r,exc,d,srt):
    fst=None
    snc=None
    for i in range(0,len(r)):
        if i in exc:
            continue
        if fst is None:
            fst=i
            prev=i
            continue
        if snc is None:
            snc= i
        curr=i
        if (r[curr]-r[prev])*srt < 0\
        or abs(r[curr] - r[prev])>3\
        or abs(r[curr] - r[prev])<1:
            if d==limit :
                return True
            return defective(r,{**exc,prev:None},d+1,srt) and defective(r,{**exc,curr:None},d+1,srt)
        prev=curr

    return False

reports=[]

with open('input.txt', 'r') as file:
    for line in file:
        reports.append(line.split())

for i in range(len(reports)):
    for j in range(len(reports[i])):
        reports[i][j]=int(reports[i][j])
        

c=0
for r in reports:
    exc={}
    limit=1
    if defective(r,exc,0,-1) and defective(r,exc,0,1):
        c+=1

print(len(reports)-c)

