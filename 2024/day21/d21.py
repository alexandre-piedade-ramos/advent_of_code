def main():
    with open("test.txt") as file:
        input=[e.strip() for e in file]
    input=input
    nmap={'7':(0,0),'8':(0,1),'9':(0,2),'4':(1,0),'5':(1,1),'6':(1,2),'1':(2,0),'2':(2,1), '3':(2,2),'0':(3,1),'A':(3,2),None:(3,0)}
    sum=0
    for key in input:
        print(key)
        y,x=nmap['A']
        paths=['']
        for e in key:
            dy,dx=nmap[e][0]-y,nmap[e][1]-x
            subpaths=perms(dy,dx)
            subpaths=[p+'A' for p in subpaths if sim(nmap,y,x,p)]
            
            temp=[]
            for i in paths:
                for j in subpaths:
                    temp.append(i+j)
            paths=temp

            y,x=y+dy,x+dx
        
        print(paths)
        temp=[]
        for p in paths:
            subpaths=directional(p)
            for sp in subpaths:
                temp.append(sp)
        temp2=[]
        for p in temp:
            subpaths=directional(p)
            #print(p)
            for sp in subpaths:
                temp2.append(sp)
        temp2.sort(key=lambda e:len(e))
        print(len(temp2[0]),'*',int(key[0:-1]),'=',len(temp2[0])*int(key[0:-1]))
        sum+=len(temp2[0])*int(key[0:-1])
    print(sum)
def directional(targets):
    dmap={'^':(0,1),'A':(0,2),'<':(1,0),'v':(1,1),'>':(1,2),None:(0,0)}
    paths=['']
    y,x=dmap['A']
    for e in targets:
        dy,dx=dmap[e][0]-y,dmap[e][1]-x
        subpaths=perms(dy,dx)
        if subpaths: subpaths=[p+'A' for p in subpaths if sim(dmap,y,x,p)]
        else :       subpaths=['A']
        #print(subpaths)
        temp=[]
        for i in paths:
            for j in subpaths:
                temp.append(i+j)
        paths=temp
        y,x=y+dy,x+dx
    return paths

def sort_keys():
    dirs={'<', '>', 'v', '^'}
    res=[]
    queue=[]
    for e in dirs:
        queue.append(e)
    while queue:
        idk=queue.pop(0)
        if len(idk)==4:
            res.append(idk)
        for e in dirs-set(list(idk)):
            queue.append(idk+e)

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

def sim(map,y,x,moves):
    dirs={'^':(-1,0), '>':(0,1),'v':(1,0),'<':(0,-1)}
    for e in moves:
        dy,dx=dirs[e]
        y,x=y+dy,x+dx
        if map[None]==(y,x): return False
    return True

main()