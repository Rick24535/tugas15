from flask import Flask
import psycopg2
import os

app = Flask(__name__)

# Gunakan connection string dari Supabase
DATABASE_URL = "postgresql://postgres:[YOUR-PASSWORD]@db.vczirrnzbexdbuxcfrvg.supabase.co:5432/postgres"

# Connect to PostgreSQL database
def connect_db():
    conn = psycopg2.connect(DATABASE_URL)
    return conn

@app.route('/')
def index():
    try:
        conn = connect_db()
        cur = conn.cursor()
        # Sesuaikan query ini dengan tabel di database Supabase Anda
        cur.execute('SELECT * FROM your_table')  
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return {'data': rows}
    except Exception as e:
        return {'error': str(e)}

if __name__ == '__main__':
    app.run(debug=True)
