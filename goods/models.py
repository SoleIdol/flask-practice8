# author:Sole_idol
# filename: models.py
# datetime:2020/8/20 20:54
from libs.orm import db


class Goods(db.Model):
    __tablename__ = 'goods'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    num = db.Column(db.Integer, default=0)
    money = db.Column(db.Integer)
