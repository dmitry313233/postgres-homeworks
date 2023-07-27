"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv


# connect to db
def add_data_to_customers(path='./north_data/customers_data.csv'):
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
        # create cursor
        cur = conn.cursor()
        cur.executemany('INSERT INTO customers VALUES(%s, %s, %s)', ls_content[1:])
        conn.commit()
        # close cursor mand connection
        conn.close()


def add_data_to_employees(path='./north_data/employees_data.csv'):
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

        # create cursor
        cur = conn.cursor()
        cur.executemany('INSERT INTO employees VALUES(%s, %s, %s, %s, %s, %s)', ls_content[1:])
        conn.commit()
        # close cursor mand connection
        conn.close()


#
def add_to_orders_data(path='./north_data/orders_data.csv'):
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

        # create cursor
        cur = conn.cursor()
        cur.executemany('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)', ls_content[1:])
        conn.commit()
        # close cursor mand connection
        conn.close()


add_data_to_customers()
add_data_to_employees()
add_to_orders_data()
