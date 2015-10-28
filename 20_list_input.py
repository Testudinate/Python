Напишите программу, на вход которой подается одна строка с целыми числами. 
Программа должна вывести сумму этих чисел.

Используйте метод split строки. 

# put your python code here
s = [ int(i) for i in input().split()]
summ = 0 
l = len(s)-1
for i in range(0,l+1):
    summ = summ + s[i]
print(summ)
