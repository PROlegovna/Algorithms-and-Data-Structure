### 6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток. После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число, чем то, что загадано. Если за 10 попыток число не отгадано, вывести ответ.

from random import randint

num = randint(0, 100)

for i in range(10):
    user_num = int(input('Enter a number: '))
    if num == user_num:
        print(f'You guessed the number from {i} tries!')
        break
    elif num < user_num:
        print('The number is smaller')
    elif num > user_num:
        print('The number is bigger')
else:
    print(f'You have lost. The number was {num}')