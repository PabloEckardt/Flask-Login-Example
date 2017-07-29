# Flask-Login-Example

This is my personal take on how to structure a simple project that supports login capabilities in a scalable way.
## setup so you can run it locally using virtual environments.

###  how to run:

1. clone the repository
2. ```cd``` into the project
2. on your terminal type: ```virtualenv venv ``` you will need to have virtualenv installed as well as pip
3. ```. venv/bin/activate ```
4. ``` pip install -r requirements.txt```
5. ``` python db_create.py ```
5. ```python main.py```
6. on your browser go to localhost:5000

## This repo

I made this repo for future reference for myself or anyone who is interested on quickly getting
started making a website with flask where user authentication is necessary.
There are multiple ways to login users, some rely on boolean flags on session cookies, but this
method uses Flask-Login capabilities to demonstrate how to avoid ```session()``` function calls altogeher. NOTE: Using cookies
with flask-login is considered safe given it automatically handles stale cookies and general
shenanigans. Then again, this is one of many approaches, and this is a simplified implementation to get
a project started.

## Authentication methods

This method uses a database to store hashed passwords which is at the very least what you should do, if not
using an authentication server. In which case, one could remove the authentication and hashing functions from
the ```User class```, as well as the password column (hashed password column). And simply tweak the code such that
the ```login_user()``` function gets called AFTER having authenticated the user with the server.

## App's purpose

This is actually a short template I quickly put together to login home automation services. AKA: IOT.
So its meant to run in my local network... Therefore I made it such it allows for 1 user (me) to register, afterwards
it will just prompt logins. Changing this should be trivial in views.py

## App's deployment using httpd/nginx

Some minor tweaking would be necessary to make sure you are using the binaries from your virtual environment.

http://flask.pocoo.org/docs/0.12/installation/
