#imports
from flask_run import app
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
