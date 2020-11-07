"""
Программа оценивает сложность пароля.
Пользователь вводит пароль, в ответ получает оценку "сложный"/"простой"
Сложным считается пароль, состоящий как минимум из 8-ми символов,
включая цифры и алфавитные символы
"""

if __name__ == '__main__':
    pass

password = input('Введите пароль: ')

if (len(password) >= 8 and password.isalnum() and not
        password.isalpha() and not password.isnumeric()):
    print('сложный')
else:
    print('простой')
