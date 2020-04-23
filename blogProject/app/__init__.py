from .config import config
from flask import Flask
from .extensions import config_extension
from .views import config_blueprint


def create_app(config_name):
    app = Flask(__name__)
    #初始化配置文件
    app.config.from_object(config[config_name])
    # 注册蓝本
    config_blueprint(app)
    #各种扩展库的初始化
    config_extension(app)

    return app