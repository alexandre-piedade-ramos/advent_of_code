def input(file_name):
    problems=[]
    #[problem][line][Coord]
    with open(file_name,'r') as file:
        input=file.readlines()
    for i in range(0,len(input),4):
        new=[]

        l=input[i].split()
        new.append((int(l[2][2:-1]),int(l[3][2:len(l[3])])))

        l=input[i+1].split()
        new.append((int(l[2][2:-1]),int(l[3][2:len(l[3])])))

        l=input[i+2].split()
        new.append((int(l[1][2:-1]),int(l[2][2:len(l[2])])))

        problems.append(tuple(new))

    return problems


def solve(problems):
    def intercept(l):
        a,b,c,u,v,k=l[0][0],l[1][0],l[2][0],l[0][1],l[1][1],l[2][1]
        if (u*b-a*v) == 0:
            return 0
        x=(k*b-c*v)/(u*b-a*v)
        y=(c-a*x)/b

        if x%1!=0 or y%1!=0:
            return 0
        return 3*x+1*y

    cost=0
    for l in problems:
        cost+=intercept(l)
    if(cost%1!=0):
        raise "Something wrong, add checks for decimals"
    return int(cost)


problems=input("input.txt")
c1=solve(problems)
c2=solve([(l[0],l[1],(10**13+l[2][0],10**13+l[2][1])) for l in problems])
print(c1,c2)