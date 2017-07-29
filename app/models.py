from app import db, app
from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import InputRequired
from werkzeug import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = "user"

    def __repr__(self):
        return '<User %r>' % (self.user_name)

    # user model attributes
    id = db.Column(db.Integer, primary_key=True)
    _password = db.Column('password', db.String(150), nullable=False)
    account = db.Column(db.String(50), nullable=False)

    # Athentication functions

    def is_authenticated(self): # verify user obj is authenticated, if it was queried it is authenticated
        return True

    def _set_password(self, password):
        self._password = generate_password_hash(password)

    def _get_password(self):
        return self._password

    def check_password(self, password=None):
        if self._password is None:
            return False
        return check_password_hash(self._password, password)

    # Required by flask-login

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def get_id(self):  # Primary key needs to be converted into unicode, string in python3
        return str(self.id)

    # constructor
    def __init__(self, account, password):
        self.account = account
        self._set_password(password)
