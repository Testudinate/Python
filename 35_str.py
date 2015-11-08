В какой-то момент в Институте перестали понимать, 
что говорят информатики: они говорили каким-то странным набором звуков. 

В какой-то момент один из биологов раскрыл секрет 
информатиков: они использовали при общении подстановочный 
шифр, т.е. заменяли каждый символ исходного сообщения 
на соответствующий ему другой символ. Биологи раздобыли 
ключ к шифру и теперь нуждаются в помощи: 

Напишите программу, которая умеет шифровать и 
расшифровывать шифр подстановки. Программа принимает 
на вход две строки одинаковой длины, на первой строке 
записаны символы исходного алфавита, на второй строке — 
символы конечного алфавита, после чего идёт строка, 
которую нужно зашифровать переданным ключом, и ещё 
одна строка, которую нужно расшифровать.

Пусть, например, на вход программе передано:
abcd
*d%#
abacabadaba
#*%*d*%

Это значит, что символ a исходного сообщения заменяется 
на символ * в шифре, b заменяется на d, c — на % и d — на #.
Нужно зашифровать строку abacabadaba и расшифровать 
строку #*%*d*% с помощью этого шифра. Получаем следующие
строки, которые и передаём на вывод программы:
*d*%*d*#*d*
dacabac

Sample Input 1:

abcd
*d%#
abacabadaba
#*%*d*%

Sample Output 1:

*d*%*d*#*d*
dacabac


Sample Input 2:

dcba
badc
dcba
badc

Sample Output 2:

badc
dcba


# put your python code heres=st


s=str(input())
 
a=[]

#строка, которую необходимо зашифровать

for i in range(len(s)):

    si=s[i]

    a.append(si)

#print(a)

b=[]

n=str(input())

#символы шифра

for j in range(len(n)):

    sj=n[j]

    b.append(sj)

#print(b)

p={}

#инициализация словаря

for pi in range(len(s)):

    key=s[pi]

    p[key]=0

#print(p)

#актуализация словаря

j1=0

for i in range(0,len(a)):

    key=a[i]

    while j1<len(b):

        #print(j1)

        bj=b[0]

        if key in p:

            p[key]=bj

        b.remove(bj)

        #print(b)

        break

#print(p)

c=[]

si=str(input())

for si1 in range(0,len(si)):

    ci=si[si1]

    c.append(ci)

#print(c)

co=[]

for ci in range(0,len(c)):

    if c[ci] in p:

        cco=c[ci]

        pco=p[cco]

        co.append(pco)

#print(co)

d=[]

di=str(input())

for sj1 in range(0,len(di)):

    dj=di[sj1]

    d.append(dj)

#print(d)

do=[]

for di in range(0,len(d)):

    for key in p:

        pkey=key

        if p.get(key) == d[di]:

            ddo=pkey

            do.append(ddo)

#print(do)

for i in range (0,len(co)):

    print(co[i],end='')

print()

for j in range (0,len(do)):

    print(do[j],end='')
