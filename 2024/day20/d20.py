#values for testing againt part 1 example
#filename,max_cheat_steps,min_cheat_gain="test.txt",2,2

#values for part 1 input
#filename,max_cheat_steps,min_cheat_gain="input.txt",2,100

#values for testing againt part 2 example
#filename,max_cheat_steps,min_cheat_gain="test.txt",20,50

#values for testing againt part 2 input
filename,max_cheat_steps,min_cheat_gain="input.txt",20,100

with open(filename) as file:
    map=[e[1:-2] for e in file]
    map=map[1:-1]
    n=len(map)
    walls=set()
    for i in range(n):
        for j in range(n):
            if map[i][j]=='#':
                walls.add((i,j))
            elif map[i][j]=='S':
                start=(i,j)
            elif map[i][j]=='E':
                end=(i,j)

y,x=start
trace=[]
trace.append((y,x))
y,x=next((y+dy,x+dx) for dy,dx in ((-1,0),(0,1),(1,0),(0,-1)) if 0<=y+dy<n and 0<=x+dx<n and (y+dy,x+dx) not in walls)
trace.append((y,x))
while (y,x)!=end:
    y,x=next((y+dy,x+dx) for dy,dx in ((-1,0),(0,1),(1,0),(0,-1)) if 0<=y+dy<n and 0<=x+dx<n and (y+dy,x+dx) not in walls and (y+dy,x+dx)!=trace[-2])
    trace.append((y,x))

dend=dict()
for i in range(len(trace)):
    dend[trace[i]]=len(trace)-1-i

cheats=dict()
for i in range(len(trace)-1):
    y,x=trace[i]
    for dy in range(-max_cheat_steps,max_cheat_steps+1):
        for dx in range(-max_cheat_steps,max_cheat_steps+1):
            if abs(dy)+abs(dx)<=max_cheat_steps\
            and 0<=y+dy<n and 0<=x+dx<n\
            and (y+dy,x+dx) not in walls\
            and (y+dy,x+dx) in dend:
                gain=dend[(y,x)] - dend[(y+dy,x+dx)] - abs(dy) - abs(dx)
                if gain >= min_cheat_gain:
                    if not gain in cheats:
                        cheats[gain]=0
                    cheats[gain]+=1

print(sum(cheats.values()))
