# author:Sole_idol
# filename: models.py
# datetime:2020/8/20 20:54
from libs.orm import db


class User(db.Model):
    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    password = db.Column(db.String(30))
    tel = db.Column(db.String(20))
