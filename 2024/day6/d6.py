def inside(n:int,y:int,x:int):
    return 0<=x<n and 0<=y<n

def nextDir(n,y,x,dy,dx,blocks,newB):
    dirs={(-1,0):(0,1),(0,1):(1,0),(1,0):(0,-1),(0,-1):(-1,0)}
    if not inside(n,y+dy,x+dx):
        return 0,0
    if (y+dy,x+dx) in blocks or (y+dy,x+dx) in newB:
        dy,dx=dirs[(dy,dx)]
        return nextDir(n,y,x,dy,dx,blocks,newB)
    return dy,dx

def simulate(n,y,x,blocks,newB):
    dy,dx=(-1,0)
    trace=set()
    loops=False
    while (dy,dx) != (0,0):
        if (y,x,dy,dx) in trace:
            loops=True
            break
        trace.add((y,x,dy,dx))
        dy,dx=nextDir(n,y,x,dy,dx,blocks,newB)
        y,x=y+dy,x+dx
    visited=set((e[0],e[1]) for e in trace)
    return loops,visited

def solve2(n,y,x,blocks):
    loops,visited=simulate(n,y,x,blocks,set())
    visited.remove((y,x))
    newBlocks=set()
    if loops:
        return n*n-len(blocks)-1 #Guard already loops without any new blocks
    
    for newB in visited:
        if not newB in blocks and not newB in newBlocks:
            loops=simulate(n,y,x,blocks,{newB})[0]
            if loops:
                newBlocks.add(newB)
    return len(newBlocks)      


with open("input.txt",'r') as file:
    t=file.readlines()

n=len(t)
blocks=set((i,j) for i in range(n) for j in range(n) if t[i][j]=='#')
y,x=next((i,j) for i in range(n) for j in range(n) if t[i][j]=='^' )   
print("part1:",len(simulate(n,y,x,blocks,set())[1]))
print("part2:",solve2(n,y,x,blocks))

