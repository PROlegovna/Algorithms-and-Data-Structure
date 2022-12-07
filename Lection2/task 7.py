### 7. Написать программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n — любое натуральное число.

n = int(input('Enter a natural number: '))

left = sum([i for i in range(n+1)])
right = n * (n+1) / 2

if left == right:
    print(f'Equation 1+2+...+n = n(n+1)/2 is true for n = {n}')
else:
    print(f'Equation 1+2+...+n = n(n+1)/2 is false for n = {n}')