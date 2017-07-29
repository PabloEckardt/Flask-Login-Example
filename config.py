import os
basedir = os.path.abspath(os.path.dirname('app/db/'))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
