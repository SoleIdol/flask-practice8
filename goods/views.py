# author:Sole_idol
# filename: views.py
# datetime:2020/8/20 20:55
from flask import Blueprint, redirect
from goods.models import Goods

goods_bp = Blueprint('goods', __name__, url_prefix='/goods/')
goods_bp.template_folder = './templates'


@goods_bp.route('/index/')
def index():
    return '商品首页'


@goods_bp.route('/good_add/')
def good_add():
    g1 = Goods(name='可达鸭', num=367, money=58)
    return '商品首页'
