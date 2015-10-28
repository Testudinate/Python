
Напишите программу, которая выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ...
(число повторяется столько раз, чему равно). 
На вход программе передаётся положительное целое число 
n — столько элементов последовательности должна отобразить программа. 
На выходе ожидается последовательность чисел, записанных через пробел в одну строку. 

Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.

# put your python code here
p = []
t = []
M = []
n = int(input())
l = len(t)
k = 0
m = 2
for h in range(1,n+1):
    p.append(str(h))
for i in range(0,len(p)):
    if i==0:
        t.insert(l,p[i])
        k = 0
    elif i==1:        
        while i>=k:
            l = len(t)
            t.insert(l,p[i])
            k +=1
        k -=2
    elif i>1:
        while i>=k:
            l = len(t)
            t.insert(l,p[i])
            k +=1
        k =i-m
        m +=1
    l = len(t)
x = len(t)
if len(t)==1:
    print(1)
else:
    for j in range (0,x-1):
        M.append(t[j])
    for g in range(0,n):
        print(M[g],end=' ')

