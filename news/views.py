import logging, os
logger = logging.getLogger(__name__)

#imports
from news import app
from news.models import User
from flask_security import login_required

@app.route('/')
def index():
    try:
        return "All is well"
    except Exception as e:
        return str(e)


@app.route('/user/<username>')
@login_required
def userDash(username):
    """User dashboard"""
    user = User.query.filter_by(name=username).first_or_404()
    return "{}, {}, {}, {}".format(user.name, user.email, user.roles[0].name, user.roles[0].description)
