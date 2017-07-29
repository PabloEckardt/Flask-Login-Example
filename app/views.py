from flask import render_template, request, redirect, session
from flask_login import current_user, login_user, logout_user, login_required
from app import app,  login_manager
from app.db_queries import get_user_by_id, verify_login, get_user_num, register_user, \
                           get_user_by_account
import os

@login_manager.user_loader
def load_user(id):
    return get_user_by_id(id)

@app.route('/login')
@app.route('/')
def home():
    if get_user_num()>0:
        return render_template('login.html')
    else:
        return render_template('register.html')

@app.route("/register_user", methods=["POST"])
def register():
    if get_user_num()>0:
        return render_template('login.html')

    user_id1 = request.form["username"]
    user_id2 = request.form["username2"]
    password1 = request.form["password"]
    password2 = request.form["password2"]

    empty_field = False
    unequal_credentials = False

    if user_id1 == "" or user_id2 == ""  or password1 == "" or password2 == "":
        empty_field = True

    if not user_id1 == user_id2 or not password1 == password2:
        unequal_credentials = True

    if not empty_field and not unequal_credentials:
        register_user(user_id1, password1)
        return redirect("/target")
    else:
        return render_template("register.html")


@app.route('/target')
@login_required
def target():
    return render_template("target.html")

@app.route('/login_user', methods=['POST', "GET"])
def login_():
    if request.method == "POST": # double sure
        account = request.form["username"]
        password = request.form["password"]
        u = get_user_by_account(account)
        if verify_login(account, password):
            login_user(u)
        else:
            return home()
        return redirect("/target")
    else:
        return redirect("/")

@app.route("/logout")
@login_required
def logout():
    session.clear()
    logout_user()
    return redirect('/')

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0', port=5000)

