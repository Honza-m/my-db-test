#connect
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(Flask('views'))

#models
user_roles = db.Table('user_roles',
    db.Column('user_id', db.Integer, db.ForeignKey('user.user_id')),
    db.Column('role_id', db.Integer, db.ForeignKey('role.role_id'))
)
class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    psswd = db.Column(db.String(50), unique=True, nullable=False)
    role = db.relationship('Role', secondary=user_roles, backref="user", lazy=True)

    def __repr__(self):
        return "<User {}>".format(self.name)

class Role(db.Model):
    role_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    description = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return "<Role {}>".format(self.name)
