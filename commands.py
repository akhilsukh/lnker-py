import psycopg2
from app import app, db, URI


@app.cli.command('create_db')
def create_db():
    connection = psycopg2.connect(URI)
    cursor = connection.cursor()
    cursor.execute(f"CREATE TABLE links (code text, link text, visits int)")
    connection.commit()
    connection.close()
