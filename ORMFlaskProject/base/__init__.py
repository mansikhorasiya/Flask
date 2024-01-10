from flask import Flask
import warnings
from datetime import timedelta


from flask_sqlalchemy import SQLAlchemy

# from flask_migrate import Migrate

# pip uninstall flask-sqlalchemy

warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

app = Flask(__name__)

app.secret_key = '123456'

app.config['SQLALCHEMY_ECHO'] = True

app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)

app.config['SQLALCHEMY_DATABASE_URI'] = \
    'mysql+pymysql://root:root@localhost:3306/flaskdb'

app.config['SQLALCHEMY_MAX_OVERFLOW'] = 0

db = SQLAlchemy(app)
app.app_context().push()

# migrate = Migrate(app, db)

from base.com import controller
