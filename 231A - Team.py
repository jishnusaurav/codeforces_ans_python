ni=int(input())
l=[]
while(ni):
    l.append(input().split(' '))
    ni=ni-1


count=0
sum1=0
for i in l:
    i=[int(j) for j in i]
    if(sum(i)>=2):
        count=count+1

print(count)
  
