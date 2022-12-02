### 3. Написать программу, которая генерирует в указанных пользователем границах:
### a. случайное целое число,
### b. случайное вещественное число,
### c. случайный символ.
### Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
import random

print('Enter the range of numbers or letters: ')
a1 = int(input('a1 = '))
a2 = int(input('a2 = '))
print('Enter real number range:')
b1 = float(input('b1 = '))
b2 = float(input('b2 = '))
print('Enter random letter range:')
c1 = input('c1 = ').upper()
c2 = input('c2 = ').upper()

r_int = random.randint(a1, a2)
r_float = random.uniform(b1, b2)
r_char = chr(random.randint(ord(c1), ord(c2)))

print(f'Random number range: {r_int}\n'
      f'Real number range: {r_float}\n'
      f'Letter range: "{r_char}"')


