# Программа считает Топ-100 слов для переданного ей текстого файла.
# Путь до текстового файла передается программе в виде аргумента
# В выводе не должно быть стоп-слов (междометий, союзов, местоимений и т.д.)
# Список стоп-слов можно взять из популярного пакета nltk
# Тебе может понадобится модуль os, модуль argparse, цикл и словарь

import os
import nltk
import argparse
from gensim.parsing.preprocessing import remove_stopwords # предобработка стоп-слов

LIMIT = 100
 
def get_words(filename):  # функция разбора файла по словам для последующей обработки
 
    with open(filename, encoding="utf8") as file:    # открываем файл в кодировке utf-8
        text = file.read()    # открываем файл
    # удаляем символы переноса строки, запятиые, точки, запятиые с пробелами, знак вопрос, восклицательный знак,
    # переводим все слова в нижний регистр
    text = text.replace("\n", " ")
    text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
    text = text.lower()
    text = remove_stopwords(text.strip().lower())  # удаляем стоп-слова
    words = text.split()  # разделитель пробел
    words.sort()    # Сортировка элементов массива методом .sort() производится по умолчанию в алфавитном порядке,
    # а также от меньшего значения к большему
    return words
 
 
def get_words_dict(words):  # функция получения словаря из слов
    words_dict = dict()
 
    for word in words:  # цикл обработки слов в словаре, осуществляющий подсчет количества вхождения слов в словаре
        if word in words_dict:
            words_dict[word] = words_dict[word] + 1
        else:
            words_dict[word] = 1
    return words_dict
 
 
def main():
    filename = input("Введите путь к файлу: ")
    if not os.path.exists(filename):
        print("Указанный файл не существует")
    else:
        os.path.isfile(file_path := sys.argv[1])
        print(count_top_eng(file_path, LIMIT)) # осуществляем подсчет количества слов с ранее установленным лимитом 100