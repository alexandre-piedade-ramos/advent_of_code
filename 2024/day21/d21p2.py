from functools import cache

def main():
    with open("input.txt") as file:
        input=[e.strip() for e in file]
    nmap={'7':(0,0),'8':(0,1),'9':(0,2),'4':(1,0),'5':(1,1),'6':(1,2),'1':(2,0),'2':(2,1), '3':(2,2),'0':(3,1),'A':(3,2),None:(3,0)}
    sum=0
    for key in input:
        print(key)
        y,x=nmap['A']
        paths=['']
        for e in key:
            dy,dx=nmap[e][0]-y,nmap[e][1]-x
            subpaths=perms(dy,dx)
            subpaths=[p+'A' for p in subpaths if simN(y,x,p)]
            paths=[i+j for i in paths for j in subpaths]
            y,x=y+dy,x+dx
        
        all=[]
        for p in paths:
            res=0
            for c,n in zip('A'+p,p):
                idk=final_path(c, n,1)
                res+=idk
            all.append(res)
        sum+=min(all)*int(key[0:-1])
    print(sum)

@cache
def final_path(cur,next,depth):
    #print((depth+1)*'\t',f"final_path({cur},{next},{depth})")
    dmap={'^':(0,1),'A':(0,2),'<':(1,0),'v':(1,1),'>':(1,2),None:(0,0)}
    y,x=dmap[cur][0],dmap[cur][1]
    dy,dx=dmap[next][0]-y,dmap[next][1]-x
    if cur==next: paths=['A']
    else:         paths=[p+'A' for p in perms(dy,dx) if simD(y,x,p)]

    if depth==25:  return min([len(e) for e in paths])

    all=[]
    for p in paths:
        res=0
        for c,n in zip('A'+p, p):
            idk=final_path(c, n, depth+1)
            res+=idk
        all.append(res)
    return min(all)

@cache
def perms(dy,dx):
    dyn,dxn=abs(dy),abs(dx)
    dirs={ (-1,0):'^', (0,1):'>', (1,0):'v', (0,-1):'<'}
    moves={'<':0, '>':0, 'v':0, '^':0}
    if dy!=0: moves[dirs[(dy//abs(dy),0)]]+=dyn
    if dx!=0: moves[dirs[(0,dx//abs(dx))]]+=dxn

    res=[]
    queue=[]

    for k in moves:
        if moves[k]>0:
            new_moves=moves.copy()
            new_moves[k]-=1
            queue.append((k,new_moves))

    while queue:
        path,moves=queue.pop(0)
        if len(path)==(dyn+dxn):
            res.append(path)
            continue
        for k in moves:
            if moves[k]>0:
                new_moves=moves.copy()
                new_moves[k]-=1
                queue.append((path+k,new_moves))
    return res

def simN(y,x,moves):
    nmap={'7':(0,0),'8':(0,1),'9':(0,2),'4':(1,0),'5':(1,1),'6':(1,2),'1':(2,0),'2':(2,1), '3':(2,2),'0':(3,1),'A':(3,2),None:(3,0)}
    dirs={'^':(-1,0), '>':(0,1),'v':(1,0),'<':(0,-1)}
    for e in moves:
        dy,dx=dirs[e]
        y,x=y+dy,x+dx
        if nmap[None]==(y,x): return False
    return True

@cache
def simD(y,x,moves):
    dmap={'^':(0,1),'A':(0,2),'<':(1,0),'v':(1,1),'>':(1,2),None:(0,0)}
    dirs={'^':(-1,0), '>':(0,1),'v':(1,0),'<':(0,-1)}
    for e in moves:
        dy,dx=dirs[e]
        y,x=y+dy,x+dx
        if dmap[None]==(y,x): return False
    return True
main()