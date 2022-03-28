# Внимание! Используемый метод шифрования не является абсолютной гарантией безопасности хранимых данных
from cryptography.fernet import Fernet
import os.path


# Создание ключа шифрования
def write_key():
    file_exists = os.path.exists('key.key')
    if file_exists == False:
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)


write_key()


# Загрузка ключа шифрования
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)  # Инициализация encryption модуля


# Список read/write функций
# =====================================================================================================================
# Просмотр данных
def view():
    # Вывод каждой пары логин-пароль на консоль
    file_exists = os.path.exists('datavault.txt')
    if file_exists == False:
        print("Нет данных")
        raise Exception("Нет данных")
    with open('datavault.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()  # Удаление "пустой" строчки (\n)
            login, passwd = data.split("|")  # Разделение логина и пароля при выведении на экран. ["login", "passwd"]
            print("Логин:", login, "| Пароль:", fer.decrypt(passwd.encode()).decode())


# Добавление данных
def add():
    login = input("Введите логин: ")
    passwd = input("Введите пароль: ")

    # Создание файла, если он не существует. Добавление в него информации, закрытие файла.
    with open('datavault.txt', 'a') as f:
        f.write(login + "|" + fer.encrypt(passwd.encode()).decode() + "\n")


# =====================================================================================================================
# Просмотр или добавление паролей, иначе выведение ошибки
while True:
    mode = input("[1]Добавить пароль\n[2]Просмотреть существующие пароли\n[3]Выход\n")
    if mode == "3":  # Выход из программы по условию
        break
    if mode == "1":  # Добавление пароля
        add()
    elif mode == "2":  # Просмотр сохраненных данных
        view()
    else:
        print("Выберите действие путём ввода 1 или 2.")
        continue
