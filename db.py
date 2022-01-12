import sqlite3
import psycopg2
import os

DATABASE_URL = os.environ.get("DATABASE_URL")


def get_all():
    connection = psycopg2.connect(DATABASE_URL)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM links')
    rows = cursor.fetchall()
    connection.close()
    return rows


def get_link(cursor, code):
    cursor.execute(f"SELECT link FROM links WHERE code = '{code}'")
    rows = cursor.fetchall()
    return None if len(rows) == 0 else rows[0][0]


def get_redirect(code, inc):
    connection = psycopg2.connect(DATABASE_URL)
    cursor = connection.cursor()
    res = get_link(cursor, code)
    if inc:
        cursor.execute(f"UPDATE links SET visits = visits + 1 WHERE code = '{code}'")
        connection.commit()
    connection.close()
    return res


def create_redirect(code, link):
    connection = psycopg2.connect(DATABASE_URL)
    cursor = connection.cursor()
    if get_link(cursor, code):
        return False
    cursor.execute(f"INSERT into links (code, link, visits) VALUES ('{code}', '{link}', 0)")
    connection.commit()
    connection.close()
    return True


def create_db():
    connection = psycopg2.connect(DATABASE_URL)
    cursor = connection.cursor()
    cursor.execute(f"CREATE TABLE links (code text, link text, visits int)")
    connection.commit()
    connection.close()

