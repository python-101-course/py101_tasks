"""
Программа считает Топ-100 слов для переданного ей текстого файла.

Путь до текстового файла передается программе в виде аргумента
В выводе не должно быть стоп-слов (междометий, союзов, местоимений и т.д.)
Список стоп-слов можно взять из популярного пакета nltk

Тебе может понадобится модуль os, модуль argparse, цикл и словарь
"""
import sys
import string
from collections import Counter
from nltk import word_tokenize
from nltk.corpus import stopwords

if __name__ == '__main__':
    file_path = sys.argv[1]
    with open(file_path, "r") as f:
        text = f.read()
    stop = stopwords.words('english') + list(string.punctuation)
    valid_words = [token for token in word_tokenize(text.lower()) if token not in stop]
    print(Counter(valid_words).most_common(100))
