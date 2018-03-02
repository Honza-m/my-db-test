from flask import Flask
app = Flask(__name__)

#imports
import os, psycopg2

@app.route('/')
def index():
    try:
        DATABASE_URL = os.environ['DATABASE_URL']
        con = psycopg2.connect(DATABASE_URL, sslmode='require')
        cur = conn.cursor()
        r = cur.execute("""SELECT * FROM Users""")
        return str(r)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
