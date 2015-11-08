Напишите функцию f(x), которая возвращает значение следующей функции, определённой на всей числовой прямой:

f(x)=⎧⎩⎨⎪⎪1−(x+2)2,−x2,(x−2)2+1,при x≤−2при −2<x≤2при 2<x

Требуется реализовать только функцию, решение не должно осуществлять операций ввода-вывода.

Sample Input 1:

4.5

Sample Output 1:

7.25


Sample Input 2:

-4.5

Sample Output 2:

-5.25


Sample Input 3:

1

Sample Output 3:

-0.5

def f(x):
    # put your python code here
    if x<=-2:
        f=1-(x+2)**2
    elif x>-2 and x<=2:
        f=-(x/2)
    elif x>2:
        f=(x-2)**2+1
    return f
