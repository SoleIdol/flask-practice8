# author:Sole_idol
# filename: manage.py
# datetime:2020/8/19 7:59
"""
蓝图测试练习
"""
from flask import Flask, render_template
from flask_script import Manager
from flask_migrate import MigrateCommand, Migrate

from libs.orm import db
from user.views import user_bp
from goods.views import goods_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sole:000210wibt@localhost:3306/goods'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  # 每次请求结束后都会自动提交数据库中的变动
db.init_app(app)  # 后期绑定app对象，相当于db = SQLAlchemy(app)
manage = Manager(app)
migrate = Migrate(app, db)
manage.add_command('db', MigrateCommand)

# 注册蓝图
app.register_blueprint(user_bp)
app.register_blueprint(goods_bp)


@app.route('/')
def index():
    return "render_template('/user/login/', code=301)"


if __name__ == '__main__':
    manage.run()
