### 2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

natural_n = input('Enter a natural number: ')
odd = 0
even = 0
for num in natural_n:
    if int(num) % 2 == 0:
        even +=1
    else:
        odd += 1
print(f'There are {odd} odd and {even} even digits in {natural_n}')