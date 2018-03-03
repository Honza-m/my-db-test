import logging, os
logger = logging.getLogger(__name__)
ch = logging.StreamHandler()
frmt = logging.Formatter(logging.BASIC_FORMAT)
ch.setFormatter(frmt)
logger.addHandler(ch)

from flask import Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

#imports
from models import User

@app.route('/')
def index():
    try:
        return "All is well"
    except Exception as e:
        return str(e)

@app.route('/user/<username>')
def userDash(username):
    user = User.query.filter_by(name=username).first_or_404()
    return "{}, {}, {}, {}".format(user.name, user.email, user.role.name, user.role.description)

if __name__ == '__main__':
    import views
    app.run(debug=True)
