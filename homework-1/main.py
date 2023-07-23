"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv


#connect to db
def add_data_to_customers(path = './north_data/customers_data.csv'):
    with open(path, 'r') as file:
        content = csv.reader(file, delimiter=',')
        ls_content = []
        for i in content:
            ls_content.append(i)
        conn = psycopg2.connect(
        host='localhost',
        database='north',
        user='postgres',
        password='qwerty'
)
        #create cursor
        cur = conn.cursor()
        cur.executemany('INSERT INTO customers VALUES(%s, %s, %s)', ls_content[1:])
        conn.commit()
        #close cursor mand connection
        conn.close()



#add_data_to_customers()



#- Написать скрипт в `main.py`, который заполнит созданные таблицы данными из `north_data`
#- Для подключения к БД использовать библиотеку `psycopg2`
#- Зайти в pgAdmin и убедиться, что данные в таблицах есть

