b=int(input())
x=[]
a=list(input().split())
for i in range(b):
    for j in range(i+1,b):
        if a[i]==a[j] and a[i] not in x:
            x.append(a[i])
print(' '.join(x))
