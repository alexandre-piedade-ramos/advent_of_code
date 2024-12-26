from os import system as os_system
from time import sleep as time_sleep

def main():
    filename,n,idk="input.txt",71,1024
    #filename,n,idk="test.txt",7,12
    
    with open(filename,'r') as file:
        bad=set()
        badl=list()
        for l in file:
            t=l[0:-1].split(',')
            bad.add(tuple([int(t[i]) for i in range(1,-1,-1)]))
            badl.append(tuple([int(t[i]) for i in range(1,-1,-1)]))

    
    draw=False
    if draw:
        os_system('clear')
        #time_sleep(3)
    #"""
    best=bfs(n,bad & set(badl[0:1024]),draw)
    #"""
    """
    #no real reason it should be better than bfs for this
    printMap(n,0,0,bad & set(badl[0:1024]),True)
    best=[[None for j in range(n)] for i in range(n)]
    best[0][0]=(0,0)
    a_star(n,bad & set(badl[0:1024]),best)
    """
    """
    #Couldnt get it to work
    printMap(n,0,0,bad & set(badl[0:1024]),True)
    best=id_a_star(n,bad & set(badl[0:1024]))
    """
    
    path=rebuildPath(n,best)
    p1res=f"\n\nP1: {len(path)}"
    

    up,down=len(badl),0
    #draw=True
    while up-down > 1:
        mid=(up + down)//2  
        if(draw):
            print(f"\nBinSearch : walls[0:{mid}]")
        best1=bfs(n, bad & set(badl[0:mid]), draw)
        if(draw):
            print(f"\nBinSearch : walls[0:{up}]")
        best2=bfs(n, bad & set(badl[0:up]), draw)
        
        if best1[n-1][n-1] is None:
            up = mid 
        elif best2[n-1][n-1] is None:
            down = mid  
        else:
            break
    #draw=True
    best=bfs(n,bad & set(badl[0:up]),draw)
    print(p1res,f'\nP2: bestPath[{n-1}][{n-1}]:{best[n-1][n-1]} => (x,y): {badl[up-1][1]},{badl[up-1][0]}')

    #time_sleep(5)

def bfs(n,bad,draw:bool):
    if draw:
        printMap(n,0,0,bad,draw)
    best=[[None for j in range(n)] for i in range(n)]
    best[0][0]=(0,0)
    queue=[]
    y,x=0,0
    py,px=y,x
    queue.append((y,x))
    it=0
    while len(queue)>it:
        y,x=queue[it]
        diffPrint(n,y,x,py,px,draw)
        py,px=y,x
        edges=getEdges(n,bad,y,x,best)
        for e in edges:
            best[e[0]][e[1]]=(y,x)
            queue.append(e)
        it+=1
    return best

def a_star(n,bad,best):
    cost=[[None for j in range(n)] for i in range(n)]
    cost[0][0]=0
    border=[]
    y,x=0,0
    py,px=0,0
    while (y,x)!=(n-1,n-1):
        diffPrint(n,y,x,py,True)
        py,px=y,x
        edges=getEdges(n,bad,y,x,best)
        for e in edges:
            best[e[0]][e[1]]=y,x
            cost[e[0]][e[1]]=cost[y][x]+1   
        min_queue_add(n,border,edges,cost)        
        y,x=min_queue_pop(border)
    diffPrint(n,y,x,py,px,True)

#Can't get it to work
def id_a_star(n,bad):
    limit=2*n-2
    while True:
        cut=[]
        printMap(n,0,0,bad,True)
        best=[[None for j in range(n)] for i in range(n)]
        best[0][0]=(0,0)
        cost=[[None for j in range(n)] for i in range(n)]
        cost[0][0]=0
        border=[(0,0)]
        y,x=0,0
        py,px=0,0
        while len(border)>0:
            if (y,x)==(n-1,n-1):
                return best
            y,x=min_queue_pop(border)
            diffPrint(n,y,x,py,px,True)
            py,px=y,x
            edges=getEdges(n,bad,y,x,best)
            for e in edges:
                old_cost=cost[e[0]][e[1]]
                new_cost=cost[y][x]+1
                if old_cost is None or new_cost<old_cost:
                    best[e[0]][e[1]]=y,x
                    cost[e[0]][e[1]]=new_cost
                if cost[e[0]][e[1]]>limit:
                    cut.append(f(n,e[0],e[1],cost[e[0]][e[1]]))
                    continue    
                min_queue_add(n,border,[e],cost)
        limit=min(cut)
        print(cut)
        diffPrint(n,y,x,py,px,True)

def min_queue_add(n,border,edges,cost):
    border.extend(edges)
    #i know, i know
    border.sort(key=lambda e: f(n,e[0],e[1],cost[e[0]][e[1]]), reverse=True)
    return

def min_queue_pop(border:list):
    return border.pop()

def getEdges(n,bad,y,x,best):
    edges=[]
    for dy,dx in ((-1,0),(1,0),(0,-1),(0,+1)):
        e=(y+dy,x+dx)
        if 0<=e[0]<n and 0<=e[1]<n\
        and e not in bad\
        and best[e[0]][e[1]] is None:
                edges.append(e)
    return edges

def printMap(n,y,x,bad,draw:bool):
    if not draw:
        return
    print(f"\033[{1};{1}H", end="")
    for i in range(n):
        for j in range(n):
            if (i,j)==(y,x):
                print('@ ',end='')
            elif (i,j) in bad:
                print('# ',end='')
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
    time_sleep(0.001)
    print(f"\033[{py+1};{2*px+1}H", end="")
    print("x", end="",flush=True)
    print(f"\033[{y + 1};{2*x + 1}H", end="")
    print("@", end="",flush=True)
    print(f"\033[{n+2};{1}H", end="")
    print(y,x, end="",flush=True)

def f(n,y,x,path_cost):
    return path_cost+ 2*(n-1) - y - x 

def rebuildPath(n,best):
    path=[]
    y,x=n-1,n-1
    while (y,x)!=(0,0):
        path.append((y,x))
        y,x=best[y][x]
    return path

main()
