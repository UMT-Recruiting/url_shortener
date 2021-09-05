from flask_sqlalchemy import SQLAlchemy

database = SQLAlchemy()

class User(database.Model):
    __tablename__ = 'users'
    
    