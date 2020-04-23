from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serialize
from flask import current_app
from app.extensions import login_manager
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    password_hash = db.Column(db.String(200))
    email = db.Column(db.String(60), unique=True)
    status = db.Column(db.Boolean, default=False)
    photo = db.Column(db.String(50), default='default.jpg')


    @property
    def password(self):
        raise AttributeError('密码是不可读的')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def make_active_token(self):
        s = Serialize(current_app.config['SECRET_KEY'])
        return s.dumps({'id': self.id})

    # 验证密码输入
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


    # 定义一个验证token函数
    @staticmethod
    def check_token(token):
        s = Serialize(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        u = User.query.get(data['id'])
        if not u:
            return False
        if not u.status:
             u.status = True
             db.session.add(u)

        return True

#登录模块的回调函数
@login_manager.user_loader
def load_user(uid):
    return User.query.get(int(uid))