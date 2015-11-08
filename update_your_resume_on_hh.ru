#Скрипт для обновления резюме на HH.ru
import requests

def fun():
    access_token = '*****' #your acces token
    url = 'https://api.hh.ru/resumes/*****/publish' #your resume id
    response = requests.post(
        url , 
        headers={
        'User-Agent': 'Test/1.0 (*****@gmail.com)', #your @mail
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % access_token   
        }
    )
    print(response.status_code)
x = fun()
print('finish')
