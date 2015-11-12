l=[]
n = int(input())
s = 0
k = 0
i = 1
while s<n:
    s = s+i
    if (s<n):
        l.append(i)
        k = k + 1
        i = i+1
    elif (s>n):
        l.remove(s-n)
        l.append(i)
    elif (s==n):
        l.append(i)
        k = k + 1
print(k)
for i in range(0,k):
    print(l[i],end=' ')
