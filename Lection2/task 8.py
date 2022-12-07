### 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

n = int(input('Enter the number of digits: '))
nums = [input(f'Enter {i+1}: ') for i in range(n)]
a = input('Enter a digit: ')

result = sum([c.count(a) for c in nums])
print(f'Digit {a} appears in the row {result} time(s)')