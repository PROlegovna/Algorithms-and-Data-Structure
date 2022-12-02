### 7. Определить, является ли год, который ввел пользователь, високосным или не високосным.

year = int(input('Enter a year: '))

if year % 400 == 0:
    print(f"Year {year} is a leap year")
elif year % 100 == 0 and year % 400 != 0:
    print(f"Year {year} is not a leap year")
elif year % 4 == 0:
    print(f"Year {year} is a leap year")
else:
    print(f"Year  {year} is not a leap year")