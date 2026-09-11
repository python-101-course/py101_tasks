"""
Программа выводит на экран числа от 1 до 100 включительно, с новой строки.

Если число кратно трём, то вместо этого числа программа выводит слово "zip"
Если чисто кратно пяти, то вместо этого числа выводится слово "zap"
Если число кратно пятнадцати, то вместо этого числа выводится слово "zip-zap"

Тебе может понадобиться цикл for и ветвления
"""

def zipzup_game():
    zipzup_number = 0
for zipzup_number in range(1, 100):
        if zipzup_number % 3 == 0 and zipzup_number % 5 == 0:
            print('zip-zap')
        elif zipzup_number % 3 == 0:
            print('zip')
        elif zipzup_number % 5 == 0:
            print('zap')        
        else:
            print(zipzup_number)
if __name__ == '__main__':
    zipzap_game()