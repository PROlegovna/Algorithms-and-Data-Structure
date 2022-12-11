### 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
### Примечание: попытайтесь решить задания без использования функций max, min, sum, sorted и их аналогов, в том числе написанных самостоятельно.
### В задачах 3, 4, 5, 6, 9, если искомый элемент(ы) встречается в массиве несколько раз, используйте один любой по вашему выбору.

import random

matrix = [[random.randint(1, 10) for _ in range(3)] for _ in range(3)]

for i, line in enumerate(matrix):

    if i == 0:
        min_line = line.copy()
        for item in line:
            print(f'{item:>5}', end='')
        print()
        continue

    for idx, item in enumerate(line):
        if item < min_line[idx]:
            min_line[idx] = item
        print(f'{item:>5}', end='')
    print()

print('-' * len(min_line) * 5)

max_min = min_line[0]
for item in min_line:
    print(f'{item:>5}', end='')
    if item > max_min:
        max_min = item

print()
print(f'Maximum among minimum is = {max_min}')