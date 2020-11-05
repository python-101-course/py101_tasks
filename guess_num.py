"""
Программа генерирует число от 0 до 1_000_000 и предлагает угадать его.

Программа должна приветствовать пользователя и считывать число с клавиатуры
Если число меньше загаданного, то программа выводит сообщение о том, что число
меньше
Если больше загаданного, то программа выводит сообщение о том, что больше

Программа должна выводить сообщения-предупреждения, если:
* пользователь ввёл не число
* число не входит в обозначенный в условии диапазон
Если пользователь ничего не ввёл/ввёл "exit", то происходит выход из программы.

Тебе может понадобится модуль random, цикл while и ветвления
"""
from random import randint

if __name__ == '__main__':
    number = randint(0, 1_000_000)
    print("Hello user. I picked a number from 0 to 1000000, try to guess it :)")
    while True:
        print("Write your number here ", end="")
        user_guess_input = input()
        try:
            user_guess = int(user_guess_input)
        except:
            print("Please write a number")
            continue
        user_guess = int(user_guess_input)
        if not (0 <= user_guess <= 1_000_000):
            print("Please write a number between 0 and 1000000")
        elif (user_guess < number):
            print("Your number is smaller")
        elif (user_guess > number):
            print("Your number is bigger")
        else:
            print("You got it, nice job :)")
            break
