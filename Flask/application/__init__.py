from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) #Creates a Flask object
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SECRET_KEY'] = 'Secret_Key'
db = SQLAlchemy(app)


from application import routes