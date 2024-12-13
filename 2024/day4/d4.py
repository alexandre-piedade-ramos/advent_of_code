global count

def f(v,c):
    global count
    if c=='X':
        return 1
    if v==1 and c=='M':
        return 2
    if v==2 and c=='A':
        return 3
    if v==3 and c=='S':
        count+=1
        return 4
    return 0

def b(v,c):
    global count
    if c=='S':
        return 1
    if v==1 and c=='A':
        return 2
    if v==2 and c=='M':
        return 3
    if v==3 and c=='X':
        count+=1
        return 4
    return 0

def diagonals(data,x,y):
        global count

        for i in range(y):
            it=zip(range(i,y),range(x))
            v1,v2=0,0
            for k,l in it:
                c=data[k][l]
                v1,v2=f(v1,c),b(v2,c)

        for i in range(1,x):
            it=zip(range(i,x),range(y))
            v1,v2=0,0
            for k,l in it:
                c=data[l][k]
                v1,v2=f(v1,c),b(v2,c)
        #print("l2r diag:",count)


        for i in range(y):
            it=zip(range(i,y),range(x-1,-1,-1))
            v1,v2=0,0
            for k,l in it:
                c=data[k][l]
                v1,v2=f(v1,c),b(v2,c)

        for i in range(x-2,-1,-1):
            it=zip(range(i,-1,-1),range(y))
            v1,v2=0,0
            for k,l in it:
                c=data[l][k]
                v1,v2=f(v1,c),b(v2,c)
        #print("rl2 diag:",count)

        return count

def p1():
    for i in range(y):
        v1,v2=0,0
        for j in range(x):
            c=d[i][j]
            v1,v2=f(v1,c),b(v2,c)
    #print("hor:",count)

    for j in range(x):
        v1,v2=0,0
        for i in range(y):
            c=d[i][j]
            v1,v2=f(v1,c),b(v2,c)
    #print("ver:",count)

    diagonals(d,x,y)

def submatrix(d,x0,x1,y0,y1):
    new_d=["X...X"]
    #print(x0,y0,',',x1,y1)
    for i in range(y0,y1+1):
        #print(i,i+1-y0)
        new_d.append(".")
        new_d[i+1-y0]+=d[i][x0:x1+1]+"."
    new_d.append("X...X")
    
    #for i in range(len(new_d)):
    #    print(new_d[i])
    #print("\n\n")
    return new_d

d=[]
with open("input.txt", 'r') as file:
    for l in file:
        d.append(l[0:-1])

#d=["..X...",".SAMX.",".A..A.","XMAS.S",".X...."]

y,x=len(d),len(d[0])
count,c1,c2=0,0,0
p1()
c1=count
count=0

for i in range(1,y-1):
    for j in range(1,x-1):
        if d[i][j]=='A':
            count=0
            if 2==diagonals(submatrix(d,j-1,j+1,i-1,i+1),5,5):
                c2+=1
print(c1,c2)
