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
            if d==0 :
                return True
            return defective(r,{**exc,prev:None},d-1,srt) and defective(r,{**exc,curr:None},d-1,srt)
        prev=curr

    return False

reports=[]

with open('input.txt', 'r') as file:
    for line in file:
        reports.append(line.split())

for i in range(len(reports)):
    for j in range(len(reports[i])):
        reports[i][j]=int(reports[i][j])
        


def countDefective(limit):
    c=0
    for r in reports:
        exc={}
        if defective(r,exc,limit,-1) and defective(r,exc,limit,1):
            c+=1
    return c

print("p1:",len(reports)-countDefective(0))
print("p2:",len(reports)-countDefective(1))
