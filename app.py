from flask import Flask
from flask import redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, current_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash
from rgz import rgz
from Db.models import useradmin, book
from Db import db
from PIL import Image
import os
from sqlalchemy import func
from werkzeug.utils import secure_filename
from utils import save_uploaded_file


app = Flask(__name__)
app.register_blueprint(rgz)

app.secret_key = "123"
user_db = "menedjer"
host_ip = "127.0.0.1"
host_port = "5432"
database_name = "book"
password = "1234"
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user_db}:{password}@{host_ip}:{host_port}/{database_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


# Инициализация Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return useradmin.query.get(int(user_id))

app.config['UPLOAD_FOLDER'] = 'static/kartinki'

# Создание таблиц в базе данных
with app.app_context():
    db.create_all()

# Добавление пользователя, если его нет
with app.app_context():
    existing_user = useradmin.query.filter_by(username='Mark_Starchenko').first()
    if not existing_user:
        new_user = useradmin(username='Mark_Starchenko', password=generate_password_hash('mark2003'))
        db.session.add(new_user)
        db.session.commit()
        print("Пользователь добавлен успешно.")
    else:
        print("Пользователь уже существует.")

def save_uploaded_file(uploaded_file):
    return save_uploaded_file(uploaded_file, app.config['UPLOAD_FOLDER'])
