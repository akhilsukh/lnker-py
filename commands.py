import psycopg2
from db import DATABASE_URL
from app import app


@app.cli.command('create_db')
def create_db():
    connection = psycopg2.connect(DATABASE_URL)
    cursor = connection.cursor()
    cursor.execute(f"CREATE TABLE links (code text, link text, visits int)")
    connection.commit()
    connection.close()
