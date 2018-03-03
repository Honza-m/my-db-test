from flask import Flask
app = Flask(__name__)

#imports
import database

@app.route('/')
def index():
    try:
        r = database.Get("People").get_all()
        return str(r)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
