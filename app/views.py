from flask import   render_template, Blueprint, render_template,\
                    jsonify, request, redirect, session
from flask_login import current_user, login_user, \
    logout_user, login_required
from app import app,  login_manager
from models import LoginForm, User
from db_queries import get_user_by_id, verify_login
import os

@login_manager.user_loader
def load_user(id):
    return get_user_by_id(id)

@app.route('/login')
def home():
    return render_template('login.html')

@app.route('/target')
def target():
    return "login succesful"

@app.route('/login_user', methods=['POST'])
def login_():
    user_id = request.form["username"]
    password = request.form["password"]
    if verify_login(user_id, password):
        login_user()
    else:
        return home()


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0', port=5000)