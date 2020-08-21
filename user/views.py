# author:Sole_idol
# filename: views.py
# datetime:2020/8/20 20:55
from flask import Blueprint, redirect
from user.models import User

user_bp = Blueprint('user', __name__, url_prefix='/user/')
user_bp.template_folder = './templates'



@user_bp.route('/login/')
def login():
    return '用户登录网页'


@user_bp.route('/register/')
def register():
    u = User(name='jack', password='123456', tel='13822930045')
    
    return '用户注册网页'


@user_bp.route('/main/')
def main():
    return '用户主网页'


@user_bp.route('/logout/')
def logout():
    return redirect('/user/login/')
