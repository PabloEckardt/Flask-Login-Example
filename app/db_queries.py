from app.models import User
from app import db


def get_user_by_id (id):
    q = User.query.filter_by(id=int(id)).first()
    return q

def verify_login(id, password):
    u = get_user_by_id(id)
    return u.check_password(password)
