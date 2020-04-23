from flask import Blueprint, render_template, url_for
from itsdangerous import TimedJSONWebSignatureSerializer as Serialize
from flask import current_app

main = Blueprint(__name__, 'main')



@main.route('/index/')
def index():
    # s = Serialize(current_app.config['SECRET_KEY'])
    return render_template('main/index.html')