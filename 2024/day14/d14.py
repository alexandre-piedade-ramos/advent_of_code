import re
import time
def printMap(robots):
    m=[]
    for i in range(h):
        m.append([0 for j in range(w)])

    for e in robots:
        m[e[1]][e[0]]+=1

    for i in range(h):
        for j in range(w):
            e=m[i][j]
            if e==0:
                print(' ',end='')
            else:
                print('*',end='')
        print()
    print()

def avgDistFromAvg(robots):
    pos=[(e[0],e[1]) for e in robots]
    ux,uy=0,0
    for e in pos:
        ux+=e[0]
        uy+=e[1]
    u=(ux/len(pos),uy/(len(pos)))
    diff=0
    for e in pos:
        diff+=((e[0]-u[0])**2+(e[1]-u[1])**2)**(1/2)
    diff/=len(pos)
    return diff

def p1(robots):
    res=0
    sum=[0,0,0,0]
    for e in robots:
        if e[0]<(w//2) and e[1]<(h//2):
            sum[0]+=1
        elif e[0]>(w//2) and e[1]<(h//2):
            sum[1]+=1
        elif e[0]<(w//2) and e[1]>(h//2):
            sum[2]+=1
        elif e[0]>(w//2) and e[1]>(h//2):
            sum[3]+=1

    res=sum[-1]
    for i in sum[0:-1]:
        res*=i
    print("p1:",res,sum)

reg=re.compile(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)')
#file,w,h="test.txt",11,7
file,w,h="input.txt",101,103
robots=[]
with open(file,'r') as file:
    for l in file.readlines():
        robots.append(tuple([int(j) for i in reg.findall(l) for j in i]))


best=(0,robots.copy(),avgDistFromAvg(robots))
for s in range(h*w): #I think it should repeat in at most h*w s, this worked at least
    for i in range(len(robots)):
        x,y,dx,dy=robots[i]
        y=(y+dy)%h
        x=(x+dx)%w     
        robots[i]=(x,y,dx,dy)
    if s==99:
        p1(robots)        
    val=avgDistFromAvg(robots)
    if val<best[2]:
        best=(s,robots.copy(),val)

print('p2:',best[0]+1,best[2],'\n',printMap(best[1]))

