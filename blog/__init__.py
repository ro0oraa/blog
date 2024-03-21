from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
app.config['SECRET_KEY']='13de7e935207a29e4394335c3636da1e'
db=SQLAlchemy(app)
from blog import routes
from models import User,Post,Map
with app.app_context():
      db.create_all()