import re

exp = re.compile(r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\)")

with open("input.txt", 'r') as file:
    data=''.join(file.readlines())

data=exp.findall(data)
clean=[e[4:-1].split(',') for e in data]

do,sum1,sum2=True,0,0
for e in clean:
    if len(e)==2:
        sum1+=int(e[0])*int(e[1])
        if do:
            sum2+= int(e[0])*int(e[1])   
    elif len(e[0])==0:
        do=True
    else:
        do=False

print(sum1,sum2)