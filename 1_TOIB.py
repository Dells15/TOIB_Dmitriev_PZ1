import hashlib
from hashlib import sha256

def create_hash_password_sha256(password):
    # Создание хеша c помощью sha256 для значения введенного с клавиатуры.
    hash = sha256(password.encode('utf-8')) # Переменная password может содержать символы Unicode, и кодировка в UTF-8 гарантирует корректность хеша.

    return hash.hexdigest() # Метод return hash.hexdigest() преобразует внутреннее представление хеша в шестнадцатиричное значение и возвращает результат.

# Вводим значение с помощью клавиатуры и выводим результат.
password = input("Введите пароль: ")
print(f"Хешированное представление SHA-256 в виде шестнадцатеричной строки: {create_hash_password_sha256(password)}")