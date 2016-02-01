# -*- coding: utf-8 -*-
# одно из заданий в @mail.ru group
import csv
import MySQLdb
import os

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='root',
    db='test')
print("ok connection")

cursor = mydb.cursor()

lis = []
for top, dirs, files in os.walk('C:\FILES'):
    for nm in files:
        text = (os.path.join(top,nm))
        t = os.path.split(text)
        t = os.path.splitext(t[1])
        full_name = t[0]+t[1]
        if t[1]=='.csv':
            lis.append(full_name)

CNT_LIS = len(lis)
j = 0
for j in range(CNT_LIS):
    text = lis[j]
    text = text.split('.')
    load_file = ''+str(text[0])+'.'+str(text[1])+''
    tabl = text[0]
    print(load_file)
    with open(load_file,"rb") as f:
        csv_data = csv.reader(f,delimiter=';') # читаем данные из файла и задаем разделитель ';'
        print(tabl)
        for row in csv_data:
            l = len(row)
            i = 0
            li = []
            for i in range(l):
                li.append(row[i])
                if i == 0:
                    print(row[i],'1')
                    sql_code = 'CREATE TABLE '+str(tabl)+' (row_id bigint,'+ str(row[i])+' varchar(64));'
                    print(sql_code)
                    cursor.execute(sql_code)
                    mydb.commit()
                elif i > 0:
                    print(row[i],'2')
                    sql_code = 'ALTER TABLE '+str(tabl)+' ADD '+ str(row[i]) +' varchar(64);'
                    cursor.execute(sql_code)
                    mydb.commit()
                i = i + 1
            break
        print('-----------')
        print('columns add')
        print('-----------')
    j=j+1
       
    with open(load_file,"rb") as f:
        csv_data = csv.reader(f,delimiter=';') # читаем данные из файла и задаем разделитель ';'
        next(csv_data) # игнорируем 1 строку, содержащую описание столбцов в файле
        step = 1
        for row in csv_data:
            l = len(row)
            k = 1
            for i in range(l):
                row_id = step
                if i == 0:
                    s = 'VALUES("'+ str(row_id) +'", "'+ str(row[i])+'");'
                    sql_code_1 = 'INSERT INTO '+ str(tabl)+' (row_id,'+str(li[0])+') '+ s
                    print(sql_code_1)
                    cursor.execute(sql_code_1)
                    mydb.commit()
                    row_id_for = row_id
                    step = step + 1
                elif i > 0:
                    print(row[i],'2')
                    sql_code_2 ="UPDATE "+str(tabl)+ " set "+ li[k] +"='"+ str(row[i])+ "' where row_id="+str(row_id_for)+" and "+ str(li[0]) +"="+row[0]+" ;"
                    print(sql_code_2)
                    cursor.execute(sql_code_2)
                    mydb.commit()
                    k = k + 1
cursor.close() # закрываем курсор
print('finish')
