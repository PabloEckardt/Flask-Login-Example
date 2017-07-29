from app.models import User
from app import db


def get_user_by_id (id):
    q = User.query.filter_by(id=int(id)).first()
    return q

def get_user_by_account (acc):
    q = User.query.filter_by(account=acc).first()
    return q

def verify_login(acc, password):
    u = get_user_by_account(acc)
    if u == None:
        return False
    return u.check_password(password)

def get_user_num():
    users = User.query.all()
    return len (users)


def register_user(acc, password):
   u = User(acc, password)
   db.session.add(u)
   db.session.commit()
