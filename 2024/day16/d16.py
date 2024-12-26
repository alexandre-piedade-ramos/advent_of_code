from time import sleep as time_sleep
from os import system as os_system
import heapq
def main():
    with open("input.txt") as file:
        grid=file.readlines()[1:-1]

    grid=[e[1:-2] for e in grid]
    n=len(grid)
    walls=set()
    for i in range(n):
        for j in range(n):
            if grid[i][j]=='S':
                start=(i,j)
            elif grid[i][j]=='E':
                end=(i,j)
            elif grid[i][j]=='#':
                walls.add((i,j))
    
    bestCost,bestNodes=ucs2(n,walls, start, end)
    printMap(n,end[0],end[1],walls,bestNodes,True)
    print(bestCost,len(bestNodes))
    return

def ucs(n,walls,start,end):
    border=[]
    done=set()
    y,x,dy,dx,cost=start[0],start[1],0,1,0
    min_queue_add(border, [(y,x,dy,dx,cost)])
    while border:
        print(border)
        y,x,dy,dx,cost=min_queue_pop(border)
        if (y,x)==end:
            return cost
        edges=getEdges(n,walls,y,x,dy,dx,cost,done)
        min_queue_add(border,edges)
        done.add((y,x))
    return -1 

def getEdges(n,walls,y,x,pdy,pdx,cost,done):
    edges=[]
    for dy,dx in ((-1,0),(1,0),(0,-1),(0,+1)):
        e=(y+dy,x+dx)
        if 0<=e[0]<n and 0<=e[1]<n\
        and e not in walls\
        and e not in done:
                if (dy,dx)==(pdy,pdx):
                    ecost=1
                elif (-1*dy,-1*dx)==(dy,dx):
                    ecost=1+2*1000
                else:
                    ecost=1+1*1000
                edges.append((e[0],e[1],dy,dx,cost+ecost))
    return edges

def min_queue_add(border,edges):
    #i know, i know
    border.extend(edges)
    border.sort(key=lambda e: g(e[4]),reverse=True)
    return

def min_queue_pop(border):
    return border.pop()

"""
Guarantees:
First time I reach a node with a direction, I found a shortest path there through that dir
There may be other paths just as good
If a path is optimal for the goal, it will be optimal for each node-dir along the way
"""
def ucs2(n,walls,start,end):
    optimal_nodes=set()
    border=[]
    done=dict()
    visited=set()
    cost,y,x,dy,dx,path=0,start[0],start[1],0,1,(start,)
    heapq.heappush(border, (cost,y,x,dy,dx,path))
    max_cost=None
    printMap(n,y,x,walls,optimal_nodes,True)
    py,px=y,x
    while border:
        cost,y,x,dy,dx,path=heapq.heappop(border)
        visited.add((y,x,dy,dx))
        diffPrint(n,y,x,py,px,True)
        #print(cost)
        done[(y,x,dy,dx)]=cost
        if (y,x)==end:
            if max_cost is None:
                max_cost=cost
            optimal_nodes = optimal_nodes | set(path)
            continue
        
        edges=getEdges2(n,walls,y,x,dy,dx,cost,path,done,max_cost)
        for e in edges:
            heapq.heappush(border, e)
        py,px=y,x
    print()  
    return max_cost,optimal_nodes

def printMap(n,y,x,bad,optimal,draw:bool):
    if not draw:
        return
    os_system("clear")
    print(f"\033[{1};{1}H", end="")
    for i in range(n):
        for j in range(n):
            if (i,j)==(y,x):
                print('@ ',end='')
            elif (i,j) in bad:
                print('# ',end='')
            elif (i,j) in optimal:
                print('O ',end='')
            else:
                print('. ',end='')
        print()
    print()

#At least in the gnome terminal, this will only work with enough zoom out 
#to fit the whole field drawing and with no scrolling
def diffPrint(n,y,x,py,px,draw:bool):
    if not draw:
        return
    if (y,x)==(0,0):
        return
    #time_sleep(0.1)
    print(f"\033[{py+1};{2*px+1}H", end="")
    print("x", end="",flush=True)
    print(f"\033[{y + 1};{2*x + 1}H", end="")
    print("@", end="",flush=True)
    print(f"\033[{n+2};{1}H", end="")
    print(y,x, end="",flush=True)



def getEdges2(n,walls,y,x,dy,dx,cost,path,done,max_cost):
    edges=[]
    for ndy,ndx in ((-1,0),(1,0),(0,-1),(0,+1)):
        e=(y+ndy,x+ndx)
        if 0<=y+ndy<n and 0<=x+ndx<n\
        and (y+ndy,x+ndx) not in walls:
            if (ndy,ndx)==(dy,dx):
                ecost=1
            elif (-1*ndy,-1*ndx)==(dy,dx):
                ecost=1+2*1000
            else:
                ecost=1+1*1000
            if ((y+ndy,x+ndx,ndy,ndx) not in done or done[(y+ndy,x+ndx,ndy,ndx)]>=cost+ecost)\
            and (max_cost is None or cost+ecost<=max_cost):
                edges.append((cost+ecost,e[0],e[1],ndy,ndx,path+(e,)))
    return edges

def g(path_cost):
    return path_cost 

def rebuildBestPath(start,end,best,bestdir):
    path=[]
    y,x=end
    dy,dx=next(e for ent in bestdir[y][x] for e in ent if e is not None)
    path.append((y,x,dy,dx))
    while (y,x)!=start:
        path.append(best[y][x][dy][dx]+bestdir[y][x][dy][dx])
        ny,nx=best[y][x][dy][dx]
        ndy,ndx=bestdir[y][x][dy][dx]
        y,x,dy,dx=ny,nx,ndy,ndx

    return path

def dfs(n,walls,start,end,max_cost):
    paths=[]
    stack=[]
    y,x=start
    dy,dx=(0,1)
    path=[]+[(y,x)]
    stack.append((y,x,dy,dx,0,path,set(path)))

    while len(stack)>0:
        #print(stack)
        y,x,dy,dx,cost,path,visited=stack.pop()
        
        if (y,x)==end:
            paths.append(tuple(path))
            print(path)
            continue

        edges=getEdgesDfs(n,walls,y,x,dy,dx,stack,visited)

        for ey,ex,edy,edx,ecost  in edges:
            if cost+ecost>max_cost:
                continue
            nv=visited.copy()
            nv.add((y,x))
            stack.append((ey,ex,edy,edx,cost+ecost,path+[(y,x)],nv))
        
    #print(paths)
    return paths

def getEdgesDfs(n,walls,y,x,pdy,pdx,stack,visited):
    edges=[]
    for dy,dx in ((-1,0),(1,0),(0,-1),(0,+1)):
        e=(y+dy,x+dx)
        if 0<=e[0]<n and 0<=e[1]<n\
        and e not in walls\
        and e not in visited:
            if (dy,dx)==(pdy,pdx):
                cost=1
            elif (-1*dy,-1*dx)==(dy,dx):
                cost=1+2*1000
            else:
                cost=1+1*1000
            edges.append((e[0],e[1],dy,dx,cost))
    return edges




main()