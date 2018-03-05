import logging, os, random, string
logger = logging.getLogger(__name__)
ch = logging.StreamHandler()
frmt = logging.Formatter(logging.BASIC_FORMAT)
ch.setFormatter(frmt)
logger.addHandler(ch)

import os

from flask import Flask
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "".join(random.choice(string.ascii_letters) for _ in range(10))
app.config['SECURITY_PASSWORD_SALT'] = "MWfYKxtEqBEaBY0gIntk9TFMc"
