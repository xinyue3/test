from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_uploads import  UploadSet, IMAGES, configure_uploads, patch_request_class

db = SQLAlchemy()
mail = Mail()
bootstrap = Bootstrap()
migrate = Migrate(db=db)
login_manager = LoginManager()

photo = UploadSet('photos', IMAGES)

def config_extension(app):
    login_manager.init_app(app)
    bootstrap.init_app(app)
    db.init_app(app)
    mail.init_app(app)
    migrate.init_app(app)

    #指定登录的路由
    login_manager.login_view='app.views.user.login'
    login_manager.login_message = '需要登录才可以访问'
    login_manager.session_protection = 'strong'

    # 配置文件上传的操作
    configure_uploads(app, photo)
    # 设置上传大小
    patch_request_class(app)