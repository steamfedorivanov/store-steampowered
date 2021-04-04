# импортирование модулей
from colorama import Fore, init
import sqlite3

# подключение colorama
init()


# подключение базы данных к основному приложению
class SteamDataBase:
    # инициализация базы данных
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    # добвление данных из формы
    def add_data(self, username, password):
        try:
            self.__cur.execute("INSERT INTO steamdata VALUES(NULL, ?, ?)", (username, password))
            self.__db.commit()
            print(Fore.GREEN + f'Запись о новом пользователе успешно добалена в базу данных! - {username}:{password}')
        except sqlite3.Error as error:
            print(Fore.RED + 'Ошибка добвления записи о пользователе в базу данных!\nОписание ошибки:')
            print(f'{error}')
            return False
        return True