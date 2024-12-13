def main():
    t={}
    input=[]
    with open('input.txt','r') as file:
        for line in file:
            input.append(line[0:-1])

    for line in range(len(input)):
            for col in range(len(input[line])):
                k=input[line][col]
                if k=='.':
                    continue
                t.setdefault(k,[])
                t[k].append((line,col))

    h=len(input)
    w=len(input[0])

    print(solve(t,h,w,1))
    print(solve(t,h,w,max(h,w)))

def solve(t,h,w,maxc):
    nodes=set()
    for k in t:
        for i in range(len(t[k])):
            for j in range(i+1,len(t[k])):
                dy=t[k][i][0] - t[k][j][0]
                dx=t[k][i][1] - t[k][j][1]

                c=0 if maxc>1 else 1
                ny=t[k][i][0] + c*dy
                nx=t[k][i][1]  + c*dx
                while 0<=ny<h and 0<=nx<w and c<=maxc:
                    nodes.add((ny,nx))
                    ny=t[k][i][0] + c*dy
                    nx=t[k][i][1]  + c*dx
                    c+=1
                c=0 if maxc>1 else 1
                ny=t[k][j][0] - c*dy
                nx=t[k][j][1] - c*dx
                while 0<=ny<h and 0<=nx<w and c<=maxc:
                    nodes.add((ny,nx))
                    ny=t[k][j][0] - c*dy
                    nx=t[k][j][1] - c*dx
                    c+=1
    return len(nodes)

main()
