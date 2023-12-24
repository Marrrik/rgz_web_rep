from . import db
from flask_login import UserMixin


class book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    pages = db.Column(db.Integer, nullable=False)
    publisher = db.Column(db.String(255), nullable=False)
    cover_image_url = db.Column(db.String(255), nullable=True)  # URL к фото обложки


class useradmin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

# # Пример создания пользователя и добавления его в базу данных
# # Это лучше делать через миграции SQLAlchemy, но для примера
# # я добавлю пользователя напрямую в коде
# from werkzeug.security import generate_password_hash

# # Хэширование пароля перед сохранением в базу данных
# hashed_password = generate_password_hash('mark2003', method='pbkdf2:sha256')

# # Создание объекта пользователя и добавление в базу данных
# new_user = UserAdmin(username='Starchenko Mark', password=hashed_password)
# db.session.add(new_user)
# db.session.commit()
