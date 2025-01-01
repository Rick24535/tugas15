from flask import Flask
import psycopg2

app = Flask(__name__)

# Connect to PostgreSQL database
def connect_db():
    conn = psycopg2.connect(
        host="localhost",  # akan digantikan dengan URL database di Render
        database="your_db",  # ganti dengan nama database Anda
        user="your_user",  # ganti dengan username database
        password="your_password"  # ganti dengan password database
    )
    return conn

@app.route('/')
def index():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('SELECT * FROM your_table')
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return {'data': rows}

if __name__ == '__main__':
    app.run(debug=True)
