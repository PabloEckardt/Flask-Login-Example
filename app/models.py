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
    _password = db.Column('password', db.String(db.String(150)), nullable=False)


    # Athentication functions

    def is_authenticated(self): # verify user obj is authenticated, if it was queried it is authenticated
        return True

    def _set_password(self, password):
        self._password = generate_password_hash(password)

    def _get_password(self):
        return self._password

    def check_password(self, password=None):
        if self.password is None:
            return False
        return check_password_hash(self.password, password)

    # Required by flask-login

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def get_id(self):  # Primary key needs to be converted into unicode
        return unicode(self.id)

    # constructor
    def __init__(self, account, password):
        self.account = account
        self._set_password(password)

class LoginForm(Form):
    username = TextField('Username', [InputRequired()])
    password = PasswordField('Password', [InputRequired()])