from flask import Blueprint, render_template, url_for, flash,get_flashed_messages, redirect
from app.models import User
from app.email import send_mail

#导入注册表单
from app.forms import RegisterForm, LoginForm
from app.extensions import db
from flask_login import login_user, logout_user, login_required


user = Blueprint(__name__, 'user')

@user.route('/login/', methods=['get', 'post'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        u = User.query.filter_by(username=form.username.data).first()
        if not u:
            flash('当前用户不存在')
        elif not u.status:
            flash('请先激活账户')
        elif u.check_password(form.password.data):
            login_user(u, remember=form.remember.data)
            flash('登陆成功')
            return redirect(url_for('app.views.main.index'))
        else:
            flash('请输入正确的密码')
    return render_template('user/login.html', form=form)

@user.route('/register/', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # 将数据存入数据库
        u = User(username=form.username.data, password=form.password.data, email=form.email.data)
        db.session.add(u)
        db.session.commit()

        # 生成用于验证激活的token
        token = u.make_active_token()
        print(token)
        # 发送邮件
        send_mail(u.email, '账户激活', 'email/active', username=u.username, token=token)
        flash('邮件已发送，请读取邮件并激活')
        return render_template('main/index.html')
    return render_template('user/register.html', form=form)


@user.route('/active/<token>/')
def active(token):
    if User.check_token(token):
        flash('账户激活成功')

        return render_template('main/index.html')
    else:
        flash('账户激活失败')
        return redirect(url_for('app.views.main.index'))



@user.route('/index/')
def index():
    return render_template('common/base.html')

@user.route('/logout/')
def logout():
    logout_user()
    flash('退出成功')
    return redirect(url_for('app.views.main.index'))



@user.route('/test/')
@login_required
def test():
    return '必须登录'

# 修改头像
@user.route('/change_photo/')
def changePhoto():
    pass
