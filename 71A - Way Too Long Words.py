ni=int(input())
l=[]
while(ni):
    l.append(input())
    ni=ni-1
lf=[]
for i in l:
    ns=''
    if len(i)>10:
        ns=ns+i[0]+str(len(i)-2)+i[-1]
        lf.append(ns)
    else:
        lf.append(i)

for i in lf:
    print(i)
