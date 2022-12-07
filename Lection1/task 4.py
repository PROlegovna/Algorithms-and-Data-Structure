### 4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

print('Enter two small letters:')
c1 = input('c1 = ')
c2 = input('c2 = ')

pos_c1 = ord(c1) - 1071
pos_c2 = ord(c2) - 1071
distance = abs(pos_c1 - pos_c2) - 1
print(f'Letter "{c1}" is under number {pos_c1} in the alphabet\n'
      f'Letter "{c2}" is under number {pos_c2} in the alphabet\n'
      f'There are {distance} other letters between these letters')