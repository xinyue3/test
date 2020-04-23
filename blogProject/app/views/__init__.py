from .user import user
from .main import main

# 蓝本的配置
default_blueprint = [
    [user, '/user'],
    [main, '/main']
]

def config_blueprint(app):
    for blueprint, url_prefix in default_blueprint:
        app.register_blueprint(blueprint, url_prefix=url_prefix)