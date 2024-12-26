d={'<':(0,-1),'^':(-1,0),'>':(0,1),'v':(1,0)}
filename = 'input.txt'

def inputProblem():
    with open(filename,'r') as file:
        input=file.readlines()

    n=len(input[0])
    wh=[]
    for i in range(n-1):
        wh.append(list(input[i][0:-1]))
    n-=1    
    moves=[]
    for j in range(i+2,len(input)):
        moves+=input[j][0:-1]
    return wh,moves,n

def p1():
    wh,moves,n=inputProblem()
    pos=next((i,j) for i in range(n) for j in range(n) if wh[i][j]=='@')

    for m in moves:
        dy,dx=d[m]
        y,x=pos
        c=0
        e=wh[y+c*dy][x+c*dx]
        while e!='#' and e!='.':
            c+=1
            e=wh[y+c*dy][x+c*dx]


        if e=='#':
            continue

        while e!='@' :
            e=wh[y+(c-1)*dy][x+(c-1)*dx]
            wh[y+c*dy][x+c*dx]=e
            c-=1
        wh[y][x]='.'
        c+=1
        pos=y+c*dy,x+c*dx
        #for e in wh:
        #    print(''.join(e))
        #print()

    sum=0
    for i in range(n):
        for j in range(n):
            if wh[i][j]=='O':
                sum+=i*100+j
    return sum

def p2():
    wh,moves,n=inputProblem()
    #transform the map
    temp=[]
    for l in wh:
        temp.append([])
        for e in l:
            if e=='#' or e=='.':
                temp[-1].append(e)
                temp[-1].append(e)
            elif e=='O':
                temp[-1].append('[')
                temp[-1].append(']')
            elif e=='@':
                temp[-1].append('@')
                temp[-1].append('.')
    wh=temp


    #push 'em boxes
    def push(y,x,wh,d):
        #bfs the boxes that would be pushed
        #give up if one would colide with wall
        at=y,x
        dy,dx=d
        y,x=y+dy,x+dx
        queue=[(y,x)]
        queued=set()
        queued.add((y,x))
        it=0
        while it<len(queue):
            #print(queue)
            y,x=queue[it]
            e=wh[y][x]
            
            if e=='[' and (y,x+1) not in queued:
                queue.append((y,x+1))
                queued.add((y,x+1))
            elif e==']' and (y,x-1) not in queued:
                queue.append((y,x-1))
                queued.add((y,x-1))
            y,x=y+dy,x+dx
            e=wh[y][x]
            if e=='#':
                return at
            if (e=='[' or e==']') and (y,x) not in queued:
                queue.append((y,x))
                queued.add((y,x))
            it+=1

        #push them forward front to back
        it-=1
        while it>=0:
            y,x=queue[it]
            wh[y+dy][x+dx]=wh[y][x]
            wh[y][x]='.'
            it-=1
        y,x=at
        wh[y][x]='.'
        y,x=y+dy,x+dx
        wh[y][x]='@'
        return y,x

    #the robot moves
    y,x=next((i,j) for i in range(n) for j in range(2*n) if wh[i][j]=='@')
    for m in moves:
        dy,dx=d[m]
        e=wh[y+dy][x+dx]
        if e=='#':
            continue
        elif e=='.':
            wh[y][x]='.'
            y,x=y+dy,x+dx
            wh[y][x]='@'
        else:
            y,x=push(y,x,wh,d[m])
            

    #for e in wh:
    #    print(''.join(e))
    #print()

    sum=0
    for i in range(0,n):
        for j in range(0,2*n):
            if wh[i][j]=='[':
                sum+=i*100+j
    return sum



print("p1:",p1())
print("p2:",p2())
