

def printt(t,y,x):
    print('\n',t[y][x])
    for i in range(len(t)):
        for j in range(len(t[i])):
            if t[i][j]==-2:
                print('.',end='')
            elif (i,j)==(y,x):
                print('*',end='')
            else:
                print(t[i][j],end='')
        print()

def getEdges(t,y,x,done):
    #assume square
    n=len(t)
    edges=[]
    for i,j in zip((-1,0,1,0),(0,1,0,-1)):
        if not (0<=y+i<n and 0<=x+j<n)\
        or not t[y+i][x+j]==t[y][x]+1\
        or (y+i,x+j) in done:
                continue
        edges.append((y+i,x+j))
    return edges

def dfs(t,y,x):
    done=set()
    stack=[(y,x)]
    acc=0
    while len(stack)>0:
        y,x=stack[-1]
        edges=getEdges(t,y,x,done)
        stack.extend(edges)
        if t[y][x]==9:
            acc+=1
        if len(edges)==0:
            #print(done,targets)
            done.add(stack.pop())
    return acc

def getEdges2(t,y,x,done,vals):
    #assume square
    n=len(t)
    edges=[]
    targetnum=0
    for i,j in zip((-1,0,1,0),(0,1,0,-1)):
        if not (0<=y+i<n and 0<=x+j<n)\
        or t[y+i][x+j]!=t[y][x]+1:
                continue
        
        if t[y+i][x+j]==9:
            targetnum+=1
            continue

        if (y+i,x+j) in done:
            targetnum+=vals[y+i][x+j]     
        else:
            edges.append((y+i,x+j))
    
    return targetnum,edges

def dfs2(t,y,x,done,vals):
    stack=[(y,x)]
    #print(vals)
    while len(stack)>0:
        i,j=stack[-1]
        tnum,edges=getEdges2(t,i,j,done,vals)
        if len(edges)>0:
            stack.extend(edges)
        else:
            vals[i][j]+=tnum
            done.add(stack[-1])
            stack.pop()
        #printt(t,i,j)
    return vals[y][x]


with open("input.txt",'r') as file:
    t=[]
    for line in file:
        if line[0]=='#':
            continue
        t.append([])
        for c in range(len(line)-1):
            if line[c]=='.':
                t[-1].append(-2)
            else:
                t[-1].append(int(line[c]))

sum1,sum2=0,0
s1,s2=0,0
vals=[[0 for i in range(len(t))] for j in range(len(t))]
done=set()
for i in range(len(t)):
    for j in range(len(t[i])):
        if t[i][j]==0:
            s1=dfs(t,i,j)
            s2=dfs2(t,i,j,done,vals)
            sum1+=s1
            sum2+=s2
print(sum1,sum2)