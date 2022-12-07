### 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено число 3486, надо вывести 6843.

num = int(input('Enter a natural number: '))
invers = 0

while num % 10 !=0 or num // 10 !=0:
    invers = invers * 10 + num % 10
    num //= 10
print(f'Reverse number = {invers}')