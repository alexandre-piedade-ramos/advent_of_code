def v1(blinks,line):
    for i in range(0,blinks):
        for j in range(len(line)):
            if line[j]==0:
                line[j]=1
            elif len(str(line[j]))%2==0:
                line.append(int(str(line[j])[int(len(str(line[j]))/2):len(str(line[j]))]))
                line[j]=int(str(line[j])[0:int(len(str(line[j]))/2)])
            else:
                line[j]=line[j]*2024
                #print(newl)
    print(len(line))

def v2(blinks,line):
    def rec(val,d,mem:dict):
        #print("|\t"*(6-d),(val,d))
        res=1
        if d==0:
            return res
        elif (val,d) in mem:
            res=mem[(val,d)]
        elif val==0:
            res=rec(1,d-1, mem)
        elif len(str(val))%2!=0:
            res=rec(val*2024,d-1, mem)
        else:
            v1=int(str(val)[0:int(len(str(val))/2)])
            v2=int(str(val)[int(len(str(val))/2):len(str(val))])
            res = rec(v1,d-1, mem) + rec(v2,d-1, mem)
        mem[(val,d)]=res
        return res
    
    mem=dict()
    sum=0
    for val in line:
        sum+=rec(val,blinks,mem)
    #print(mem)
    print(sum)



#Since the values are split, most subtrees have a 1 digit number as a root,
#Even large values with odd len will converge to small values quickly,
#so the problem is a great fit for memoization 

#Saw the count of distinct values values approach, that's a lot better

filename="input.txt"
with open(filename,'r') as file:
    line=file.readline()[0:-1].split()
    line=[int(e) for e in line]
    line.sort()
    #line=[1]
    print(line)

#v1(blinks,line)
v2(25,line)
v2(75,line)