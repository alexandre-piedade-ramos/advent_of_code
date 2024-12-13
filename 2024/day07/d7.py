#assume positive integers
def dfs(l,i,acc,concat:bool):
    if i==0 :
        return True if acc==0 else False
    if acc<1:
        return False
    
    if dfs(l,i-1,acc-l[i],concat):
        return True
    
    if acc%l[i]==0:
        if dfs(l,i-1,int(acc/l[i]),concat):
            return True
        
    if concat and str(acc).endswith(str(l[i])):
        acc=str(acc)[0:len(str(acc))-len(str(l[i]))]
        if acc=='':
            return True if i==1 else False
        if dfs(l,i-1,int(acc),concat):
            return True
    return False


lines=[]
with open('input.txt','r') as file:
    for line in file:
        line=line.split()
        line[0]=line[0][0:-1]
        lines.append([int(i) for i in line])

sum=0
for l in lines:
    if(dfs(l,len(l)-1,l[0],False)):
        sum+=l[0]
print(sum)

sum=0
for l in lines:
    if(dfs(l,len(l)-1,l[0],True)):
        sum+=l[0]    
print(sum)

