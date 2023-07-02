a=1
while a<=5:
    input1=input().split(' ')
    try:
        Q=(abs(a-3)+abs(input1.index("1")-2))
        break
    
    except ValueError:
        a=a+1
        continue
print(Q)
