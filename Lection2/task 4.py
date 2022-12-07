### 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.

print('The row of numbers 1, -0.5, 0.25, -0.125,...')
n = int(input('Enter the row of numbers: '))
s = 0
i = 1

for _ in range(n):
    sum += i
    i /= -2

print(f'The sum is: {s}')