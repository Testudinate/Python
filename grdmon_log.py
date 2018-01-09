#------------------------------------------------------------------------------------------------------------
#-----------------------------------------------DECLARE------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
import urllib.request #The urllib.request module defines functions and classes which help in opening URLs (mostly HTTP)
                      #in a complex world — basic and digest authentication, redirections, cookies and more.

import datetime       #The datetime module supplies classes for manipulating dates and times in both simple and complex ways.
                      #While date and time arithmetic is supported, the focus of the implementation is on efficient attribute
                      #extraction for output formatting and manipulation. For related functionality, see also the time and calendar modules.

now = datetime.datetime.now()  #Получение текущей даты\времени и сохранение в переменную now
conn = urllib.request.urlopen("http://localhost:3185/monitor.htm") # + req) #получение контента страницы

#------------------------------------------------------------------------------------------------------------
#p = ['4.0 Transitional','LABAZDC','WRUMOSB044','Guardant Net II','Dongle license limit','Loginom Studio Pro',
#'Loginom Viewer Pro','Loginom Studio Ent','Loginom Viewer Ent','Deductor Studio Ent','XXX']
#------------------------------------------------------------------------------------------------------------

p = ['Deductor Studio Ent'] #параметр необходимый для сохранения только части контента за ключевыми тегами после значения параметра p
#строки, кот. исключается и не добавляется в список
p1 = u"""b'<img align="middle" src="license.gif">&nbsp;<a href="viewobject_id0000000B.htm" target="objectparams">Deductor Studio Pro ( 0 /  0)</a>'"""  
p2 = u"""b'<img align="middle" src="license.gif">&nbsp;<a href="viewobject_id0000000C.htm" target="objectparams">Deductor Viewer Pro ( 0 /  0)</a>'"""
#пропуск строк, которые присутствуют в списке с данными для парсинга. 
p3 = u"Deductor Studio Ent"
p4 = u"Deductor Viewer Ent"
li = [] #список с данными для последующего парсинга, по умолчанию пустой
a = []  #cписок со всеми данными получаего контента страницы

#------------------------------------------------------------------------------------------------------------
#-----------------------------------------------BODY---------------------------------------------------------
#1.Сохрание всего контента страницы в список "a"
for line in conn:
    if str(line.strip())==p2 or str(line.strip())==p1:
        continue
    a.append(str(line.strip()))
#переменная для вычисления длины списка    
l = len(a)
k = 0  #счетчик для записи и парсинга основных строчек с данными
#2.Парсинг списка "а"
for j in range(0,l):
    for i in range(0,len(p)):
        #основное условие парсинга и записи данных в список "li" для последующей обработки
        if k > 0 and a[j]!="b''"and a[j]!="b'</ol>'" and a[j]!="b'<ol>'" and a[j]!="b'</html>'" and a[j]!="b'</body>'" and a[j]!="b'</font>'":
            #--отдалка 1--
            #print(a[j])
            #for ii in range(0,len(l)):
            #--отдалка 1--
            li.append(str(a[j]))
        #--отдалка 2--
        #print (a[j],"_________",p[i])
        #--отдалка 2--
        #определение строки, с которой будет начинаться парсинг
        if p[i] in a[j] and k==0:
            li.append(str(a[j]))
            k = 1 #переопределение значения переменной, которое используется в условии для парсинга списка "а"
            break #принудительное завершение условия
#--отдалка 3--        
#n = len(li)
#for g in range(0,n):
#    print(li[g],end='\n')
#--отдалка 3--

#инициализация строковых переменных начальными значениями 
st = u""   #промежуточная строковая переменная, которая используется для хранения второго элемента результата использования функции SPLIT
row = u""  #промежуточная строковая переменная, которая используется для записи данных построчно в файл 
#3.Создание TXT-файла и построчная запись распарсенных данных в файл
f = open('D:\\Program Files (x86)\\BaseGroup\\Deductor\\Deductor.txt', 'a') #а - параметр позволяет не создавать каждый раз файл, если он есть уже по указанному пути; дозапись данных
for index in range(0,len(li)):
    s = li[index].split(""""objectparams">""")  #разбиение строки по тегу для дальнейшего парсинга 
    s = s[1].replace("</a>'","")                #переопределение строки и сохранение в строковую переменную второй части разбитой строки по тегу
    s = s.replace(" (TCP/IP: ",";")             #замена текста и подготовка данных для записи в нужном разрезе в файл
    s = s.replace("\n","")                      #замена текста и подготовка данных для записи в нужном разрезе в файл
    if p3 in s:                                 #получение текста с версией ПО для записи в нужном разрезе в файл
        st = s                                  #Deductor Studio
    elif p4 in s:                               #получение текста с версией ПО для записи в нужном разрезе в файл
        st = s                                  #Deductor Viewer
    elif p4 not in s or p3 not in s:            #Построчная запись данных в нужном разрезе в файл 
        row = str(now)+u';'+st + u';'+s.upper() #Запись данных в разрезе: дата\время; версия ПО; доменное имя; IP-адрес
        f.write(row+'\n')                       #Запись данных в плоский файл                    
f.close()                                       #Завершение работы с файлом
#------------------------------------------------------------------------------------------------------------
#-----------------------------------------------THE_END------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
