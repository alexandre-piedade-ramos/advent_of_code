def solve1():
    with open("input.txt",'r') as file:
        disk=file.readline()[0:-1]
        #assume first and last value is a file
        disk+='0' #0freespace

    uncom=[]
    free=-1
    id=0
    for i in range(len(disk)):
        for j  in range(int(disk[i])):
            if free<0:
                uncom.append(str(id))
            else:
                uncom.append('.')
        if free<0:
                id+=1
        free*=-1
    compact=[]

    it=(j for j in range(len(uncom)-1,-1,-1) if uncom[j]!='.')
    d=next(it)
    for i in range(len(uncom)):
        if i>d:
            break
        if uncom[i]=='.':
            compact.append(uncom[d])
            d=next(it)
        else:
            compact.append(uncom[i])
    sum=0
    for i in range(len(compact)):
        sum+=i*int(compact[i])
    #print(uncom)
    #print(compact)
    print(sum)


def solve2():
    "input sol 6363913128533"
    with open("input.txt",'r') as file:
        disk=file.readline()[0:-1]
        #disk="12345"
        #disk="14113"
        #assume first and last value is a file
        disk+='0' #0freespace
    uncom=[]
    free=-1
    id=0
    for i in range(len(disk)):
        for j  in range(int(disk[i])):
            if free<0:
                uncom.append(str(id))
            else:
                uncom.append('.')
        if free<0:
                id+=1
        free*=-1
    #print(uncom)
    id='x'
    sz=0
    doneids=set()

    for i in range(len(uncom)-1,-1,-1):
        if id=='x': 
            if (uncom[i]=='.' or uncom[i] in doneids):
                continue
            else:
                id=uncom[i]
            
        if id==uncom[i]:
            sz+=1
            continue
        
        free=0
        for j in range(0,i+1):
            free= free+1 if uncom[j]=='.' else 0
            if free<sz:
                continue
            for l in range(0,sz):
                uncom[j-l]=uncom[i+1+l]
                uncom[i+1+l]='.'
            #print(sz,free,i,'\n',''.join(uncom))
            break

        doneids.add(id)
        id='x'
        sz=0
        if id=='x': 
            if (uncom[i]=='.' or uncom[i] in doneids):
                continue
            else:
                id=uncom[i]
            
        if id==uncom[i]:
            sz+=1
            continue
    
    sum=0
    for i in range(len(uncom)):
        if uncom[i]!='.':
            sum+=int(uncom[i])*i
    
    #print(uncom)
    print(sum)
solve1()
solve2()