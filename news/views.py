import logging, os
logger = logging.getLogger(__name__)

#imports
from news import app
from news.models import User
from flask_security import login_required, current_user

@app.route('/')
def index():
    try:
        return "All is well"
    except Exception as e:
        return str(e)


@app.route('/user')
@login_required
def userDash():
    """User dashboard"""
    user = current_user
    return "{}, {}, {}, {}".format(user.name, user.email, user.roles[0].name, user.roles[0].description)
