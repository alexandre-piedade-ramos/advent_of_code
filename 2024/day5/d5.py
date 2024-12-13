from functools import cmp_to_key

def main():
    rules,updates=parse_input("input.txt")
    #print(rules)
    #print(updates)
    print(solveSort(updates,rules))
    print(solveResolve(updates,rules))

def parse_input(fname:str):
    rules={}
    updates=[]
    with open(fname,'r') as file:
        input=file.readlines()
        m=input.index("\n")

    for e in input[0:m]:
        t=e.split('|')
        t[-1]=t[-1][0:-1]
        rules.setdefault(int(t[1]),set())
        rules[int(t[1])].add(int(t[0]))

    for e in input[m+1:len(input)]:
        t=e.split(',')
        t[-1]=t[-1][0:-1]
        for i in range(len(t)):
            t[i]=int(t[i])
        updates.append(t)
    return rules,updates

def solveResolve(updates:list,rules:dict):
    def printResolve(t,u,uset,r,sol,deps,d):
        print('\n\t'*(d-1),'resolve:')
        print('\t'*d,'t:',t)
        print('\t'*d,'u:',u)
        print('\t'*d,'uset:',uset)
        print('\t'*d,'r:',r)
        print('\t'*d,'sol:',sol)
        print('\t'*d,'deps:',deps)
        print('\t'*d,'len(deps):',len(deps))
        

    #target,update,rules,sol
    def resolve(t:int,u:list,uset:set,r:dict,sol:list,depth:int,diff:bool):
        deps=r.get(t,set()) & uset
        #printResolve(t,u,uset,r,sol,deps,depth)
        while len(deps)>0:
            new_t=next(i for i in u if i!=-1 and i in deps) #makes the sort stable I think
            diff=resolve(new_t,u,uset,r,sol,depth+1,True)
            deps=r.get(t,set()) & uset
        sol.append(t)
        uset.remove(t)
        return diff
    
    #updates=[updates[3]]
    sumDiff,sumSame=0,0
    for u in updates:
        uset=set(u)
        sol=[]
        diff=False
        for e in u:
            if not e in uset:
                continue
            relevant_rules={k:set(rules[k] & uset) for k in set(rules.keys() & uset) }
            diff=resolve(e,u,uset,relevant_rules,sol,1,diff)
        #print(diff,sol)
        middleVal=sol[len(sol)//2]
        if not diff:
            sumSame+=middleVal
        else:
            sumDiff+=middleVal
    return sumSame,sumDiff

def solveSort(updates:list,rules:dict):
    def cmp(u,v):
        if u in rules and v in rules[u]:
            return 1
        if v in rules and u in rules[v]:
            return -1
        return 0
    sumP1,sumP2=0,0

    for i in range(len(updates)):
        srtup=sorted(updates[i],key=cmp_to_key(cmp))
        val=srtup[len(srtup)//2]
        if updates[i]==srtup:
            sumP1+=val
            #print(updates[i],srtup,srtup[len(updates[i])//2])
        else:
            sumP2+=val

    return sumP1,sumP2

main()
