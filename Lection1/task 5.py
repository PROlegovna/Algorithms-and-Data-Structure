### 5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

abc_number = int(input('Enter the number of a letter in the alphabet: '))

# list of letters
abc_list = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
print(abc_list)
if abc_number <= len(abc_list):
    print(f'The letter under number {abc_number}: is  {abc_list[abc_number - 1]}')
else:
    print(
      f'The number is bigger than the number of letters ({len(abc_list)})'
    )