import logging, os
logger = logging.getLogger(__name__)
ch = logging.StreamHandler()
frmt = logging.Formatter(logging.BASIC_FORMAT)
ch.setFormatter(frmt)
logger.addHandler(ch)

from flask import Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']


if __name__ == '__main__':
    app.run(debug=True)
