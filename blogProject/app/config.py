import os

# 当前目录路径
path = os.path.abspath(os.path.dirname(__file__))

class Config():
    # 密钥
    SECRET_KEY = os.environ.get('SECRET_KEY', '123456')
    SQLALCHEMY_TRACK_MODIFICATIONS = False #配置是否追踪
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True #配置是否默认提交

    #配置是否加载本地bootstrap样式
    BOOTSTRAP_SERVEL_LOCAL = True

    # 配置smtp服务器
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.qq.com')
    # 用户名
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', '1220964574@qq.com')
    # 密码
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', 'tgcztqpoayxtgjjc')


    # 上传路径和大小
    MAX_CONTENT_LENGTH = 8*1024*1024
    UPLOADED_PHOTOS_DEST= os.path.join(path, 'static/upload')



# 配置开发环境
class DevelopmentConfig(Config):
    DEBUG = True
    # 数据库连接
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:770880@localhost/blogdevelopdatabase"


# 配置测试环境
class TestConfig(Config):
    DEBUG = False
    # 数据库连接
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:770880@localhost/blogtestdatabase"


# 配置生成环境
class ProductionConfig(Config):
    DEBUG = False
    # 数据库连接
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:770880@localhost/blogdatabase"


config = {
    'development': DevelopmentConfig,
    'test': TestConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}