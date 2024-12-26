
def main():
    with open("input.txt") as file:
        input=file.readlines()
    a=int(input[0].strip().split()[-1])
    b=int(input[1].strip().split()[-1])
    c=int(input[2].strip().split()[-1])
    p=[int(e) for e in input[4].strip().split()[-1].split(',')]
    #print(a,b,c,program)
    res1=''.join([str(e)+',' for e in p1(a,b,c,p)])[0:-1]
    print(res1)
    print(p2(p))
def combo(val,a,b,c):
        if val <= 3:
            return val
        elif val==4:
            return a
        elif val==5:
            return b
        elif val==6:
            return c
        else:
            raise "bad program"

def exec(a,b,c,inst,program):
    opcode=program[inst]
    val=program[inst+1]
    res=-1
    if opcode==0: #adv
        a= a//2**combo(val,a,b,c)
        inst+=2
    elif opcode==1:
        b= b ^ val
        inst+=2
    elif opcode==2:
        b=combo(val,a,b,c)%8
        inst+=2
    elif opcode==3:
        if a==0:
            inst+=2
        else:
            inst=val
    elif opcode==4:
        b=b^c
        inst+=2
    elif opcode==5:
        res=combo(val,a,b,c)%8
        inst+=2
    elif opcode==6:
        b= a//2**combo(val,a,b,c)
        inst+=2
    elif opcode==7:
        c= a//2**combo(val,a,b,c)
        inst+=2
    return a,b,c,inst,res

def p1(a,b,c,p):
    inst=0
    res=[]
    while(inst<len(p)):
        a,b,c,inst,r=exec(a,b,c,inst,p)
        if r>=0:
            res+=[r]

    return res

#after the last value is printed, a must be 0, otherwise it would have kept printing
def p2(p):
    queue=[0]
    while queue:
        a=queue.pop(0)
        for i in range(2**3):
            new_a=(a<<3) | i
            res=p1(new_a,0,0,p)
            if res==p[len(p)-len(res):]:
                queue.append(new_a)
                if res==p:
                    return new_a
    print(a) 
    
main()