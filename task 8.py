### 8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
## Примечания:
### Во всех заданиях, где речь идёт о буквах алфавита, решения необходимы только для строчных букв латинского алфавита от a до z.

n1, n2, n3 = [x for x in input('Enter three numbers with spaces: ').split()]

if n2 < n1 < n3 or n3 < n1 < n2:
    print(f'Average: {n1}')
elif n1 < n2 < n3 or n3 < n2 < n1:
    print(f'Average: {n2}')
else:
    print(f'Average: {n3}')