### 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

n = int(input('Enter a number of natural digits: '))
nums = [input(f'Enter {i + 1}: ') for i in range(n)]

res_max = 0
res_sum = 0

for i in nums:
    tmp_sum = sum(map(int, list(i)))
    if tmp_sum >  res_sum:
        res_sum = tmp_sum
        res_max = i

print(f'The maximum sum is {res_max}: digits sum = {res_sum}')