# study
study

[Подключение](https://meet.google.com/gvn-jhns-sdm)

SET HTTP_PROXY=http://10.0.21.52:3128

SET HTTPS_PROXY=http://10.0.21.52:3128

pip install flask flask-sqlalchemy

pip install PyMySql

pip install mysqlclient

[ИИ](https://cloud.mail.ru/public/4mcp/MNkJRQrNx)

[git](https://cloud.mail.ru/public/MvRj/piuC5Fov4)

[tcp/ip](https://cloud.mail.ru/public/4U51/RvGQnotEt)

[html/css/js](https://cloud.mail.ru/public/Vtkf/uozsHM88n)

[Демо](https://cloud.mail.ru/public/BXkt/6HbooVjbv)

[1c](https://cloud.mail.ru/public/cP9D/rG1Vb5vgg)

[git-тренажер](https://learngitbranching.js.org/?locale=ru_RU)

git remote set-url origin https://Ваш токен@github.com/Nemolite/myporject.git

git config --global http.sslVerify false

git clone https://github.com/Nemolite/myhtml.git .

[Статья](https://habr.com/ru/articles/518386/)

[gitverse](https://gitverse.ru/sergeyvushnyakov/php_study/content/master/index.php)

[front](https://sourcecraft.dev/sergey210885/front)
[back](https://gitverse.ru/sergeyvushnyakov/php_study)

[Слайдер](https://itcodik.com/article/slaydery-na-chistom-javascript----sozdanie-funkcionalnogo-slaydera-dlya-lyubogo-veb-proekta-obuchenie-programmirovaniyu-s-kodik)

# Задания на верстку
[Задание1](https://cloud.ru/)
[Задание2](https://gradum.ru/)


# 1c
[1c урок rutube](https://rutube.ru/video/db15aa69b4a4f0256a8c9fc78d0de51d/)

[Учебник](https://cloud.mail.ru/public/uD8Z/ZDMPghkia)

[Задачи](https://vk.com/wall-105441046_1169)

# ДЗ
[Задачи](https://inf-ege.sdamgia.ru/?redir=)

# ДЕМО

[Демо](https://cloud.mail.ru/public/BXkt/6HbooVjbv)


[Книги БД](https://cloud.mail.ru/public/emd9/ZWBKMoTWF)

# Book
[AI](https://cloud.mail.ru/public/9abi/2cwzCxVuq)

[pygame](https://cloud.mail.ru/public/mv9r/EpoVsQXH5)

## Django
[Django](https://cloud.mail.ru/public/yZyL/RSsKrNXXK)

[Инструкция ЦИФРИУМ](https://kb.cifrium.ru/KB/EVI_26)


[Прямая ссылка](https://app.doma.uchi.ru/u2035/31325/python/online)

[Расписание](https://app.doma.uchi.ru/u2035/31325/python/online)

[ссылка на урок](https://app.doma.uchi.ru/r/Qq3YJLdH4BoDXB4MtCuRLrzC )

============================

DATABASES = {
'default': {
'ENGINE': 'django.db.backends.mysql',
'NAME': 'djan',
'USER': 'root',
'PASSWORD': '1111',
'HOST': 'localhost',
'PORT': '3306',
}
}

[учи.ру](https://app.doma.uchi.ru/u2035/31325/python/online)

[Антонов](https://app.doma.uchi.ru/r/Nkke7wHiBmKSuki4hfLqi8qP)
[Паштынов](https://app.doma.uchi.ru/r/Vpui2sTs2GzSa3kFrthLZg1Q)
[Михайлов](https://app.doma.uchi.ru/r/5FvhFECqTN1vBR9E4UJN1i2D)
[Данилов](https://app.doma.uchi.ru/r/5fAVbetAX5RyPKdjEhET68JD)
[Тихонов](https://app.doma.uchi.ru/r/3kBJQfGmFeUDLYaXHHVvwtBh)
[Мартынов](https://app.doma.uchi.ru/r/U2m7D85dN47qYUSy5K1DWKiH)
[Александрова](https://app.doma.uchi.ru/r/cgh9pr78pRUzuXtnv3u3DTGy)
[Семаева](https://app.doma.uchi.ru/r/3XnYS3nHY629A29SVKzG5gXg)
[Исправников](https://app.doma.uchi.ru/r/mCayNTHpUK1mba3G1f39XxN4)
[Иванова](https://app.doma.uchi.ru/r/dNeK6JRDDUWX1CNjkpDbywy9)

================

from tkinter import *
from tkinter import ttk
import pymysql

def cursor_db():

  
    connection = pymysql.connect(
        host='localhost',  # хост (обычно localhost)
        port=3306,  # порт (по умолчанию 3306)
        user='root',  # имя пользователя
        password='1111',  # пароль
        database='basa2',  # имя базы данных
        charset='utf8mb4'  # кодировка для русских букв
    )

    if connection:
       return connection
    else:
        connection

root = Tk()
root.title("Работа с БД")
root.geometry("500x500")
label = ttk.Label(text="Передача данных в таблицу indef БД def", font=("Arial", 14))
label.pack()


def send_to_bd():
    connection = cursor_db()
    cursor = connection.cursor()
    id = int(entry_id.get())
    Name = entry_Name.get()
    print(id,Name)
    sql = f"INSERT INTO basa2.stud (Id, Name) VALUES ({id}, \"{Name}\")"
    print(sql)
    cursor.execute(sql)
    connection.commit()


entry_id = ttk.Entry()
entry_id.pack(anchor=NW, padx=6, pady=6)


entry_Name = ttk.Entry()
entry_Name.pack(anchor=NW, padx=6, pady=6)

btn = ttk.Button(text="Click", command=send_to_bd)
btn.pack(anchor=NW, padx=6, pady=6)


root.mainloop()
