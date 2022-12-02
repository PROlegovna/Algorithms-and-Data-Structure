### 1. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.

x = 5
y = 6

bit_and = x & y
bit_or = x | y
bit_xor = x ^ y

print(f'Fulmilment of tasks: \n'
      f'5 & 6 = {bit_and}\n'
      f'5 | 6 = {bit_or}\n'
      f'5 ^ 6 = {bit_xor}')
pass