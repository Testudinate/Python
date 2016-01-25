

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
-----------------------------------------------------------------------------------------------------------------------------------
1. Для запуска скрипта необходимо установить библиотеку requests

Installation
Do I need to install pip?
pip is already installed if you're using Python 2 >=2.7.9 or Python 3 >=3.4 downloaded from python.org, but you'll need to upgrade pip.

Additionally, pip will already be installed if you're working in a Virtual Envionment created by virtualenv or pyvenv.

Installing with get-pip.py
To install pip, securely download get-pip.py. [2]

Then run the following:

python get-pip.py

2. http://www.hinex-blog.tk/2014/11/pip-python.html

прописать переменные среды для соответствующей версии питона 

;C:\Python27;C:\Python27\Scripts\

3. Выполнить команду pip install requests


