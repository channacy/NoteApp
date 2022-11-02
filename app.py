from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_database.db'
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login.html'

if __name__ == '__main__':
    app.run(debug=True)


