input1=input()
n=int(input1.split(" ")[0])
k=int(input1.split(" ")[1])
input2=input().split(' ')
l=[f for f in input2 if (int(f) >= int(input2[k-1]) and int(f) > 0)]

print(len(l))

