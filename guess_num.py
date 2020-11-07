import random
Secret = "Я задумал число от 1 до 10."
Case = random.randint(1, 10)
print(Secret)
Attempt = 0
Input = 0
while Input != Case:
    print("Угадай число: ", end="")
    Input = int(input())
    Attempt = Attempt + 1
    if Input < Case:
        print("Слишком маленькое!")
    if Input > Case:
        print("Слишком большое!")
    if Input > 10:
        print("Ты вышел за пределы диапазона!")
    if Input == Case:
        print("Правильно!")
    if Input == 00:
        exit()
print("Ты попробовал " + str(Attempt) + " раза.")
