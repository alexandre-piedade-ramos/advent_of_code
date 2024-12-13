def getEdges(t,y,x,done):
    h,w=len(t),len(t[0])
    edges=[]
    k=0
    for i,j in zip((-1,0,1,0),(0,1,0,-1)):
        if not (0<=y+i<h and 0<=x+j<w)\
        or t[y+i][x+j]!=t[y][x]:
             continue
        if (y+i,x+j) in done:
            k+=1                
        else:
            edges.append((y+i,x+j))
    return k,edges

def bfs(t,y,x,done):
    queue=[(y,x)]
    it,area,perimeter=0,0,0
    while len(queue)>it:
        i,j=queue[it]
        #print(t[i][j],i,j)
        it+=1
        if (i,j) in done:
            continue
        k,edges=getEdges(t,i,j,done)
        queue.extend(edges)
        done.add((i,j))
        perimeter+=4-len(edges)-k
        area+=1
        k=0
    return area,perimeter

def slices(region):
    borders=0
    lh,lw=min([e[0] for e in region]),min([e[1] for e in region])
    uh,uw=max([e[0] for e in region]),max([e[1] for e in region])

    for i in range(lh-1,uh+1):
        plin,prin=False,False
        for j in range(lw-1,uw+1):
            lin,rin= (i,j) in region, (i+1,j) in region
            if (lin != rin) and (lin!=plin or rin!=prin):
                borders+=1
            plin,prin=lin,rin

    for j in range(lw-1,uw+1):
        plin,prin=False,False
        for i in range(lh-1,uh+1):
            lin,rin= (i,j) in region, (i,j+1) in region
            if (lin != rin) and (lin!=plin or rin!=prin):
                borders+=1
            plin,prin=lin,rin

    return borders

with open("input.txt",'r') as file:
    t=[l[0:-1] for l in file]
done=set()
cost1=0
cost2=0
for i in range(len(t)):
     for j in range(len(t[i])):
        if (i,j) in done:
            continue
        diff=done.copy()
        area,perimeter=bfs(t,i,j,done)
        sides=slices(list(done - diff))
        cost1+=area*perimeter
        cost2+=area*sides
        #print(t[i][j],area,perimeter,sides)
print(cost1,cost2)