"""
Программа оценивает сложность пароля.

Пользователь вводит пароль, в ответ получает оценку "сложный"/"простой"
Сложным считается пароль, состоящий как минимум из 8-ми символов,
включая цифры и алфавитные символы
"""
import re

if __name__ == '__main__':
    print("Write please your password: ", end="")
    user_password = input()
    print("сложный" if len(user_password)>=8 and re.search('[a-zA-Z]', user_password) and re.search('[0-9]', user_password) else "простой")
