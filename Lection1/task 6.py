### 6. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.

a, b, c = [
      float(x) for x in input('Enter the three length of the line segments without any signs: ').split()
        ]

if a < b + c and b < a + c and c < a + b:
    if a == b and b == c:
        print(f'The triangle with the lines {a} {b} {c} is equilateral')
    elif a == b or b == c or c == a:
        print(f'The triangle with the lines {a} {b} {c} is isosceles')
    else:
        print(f'The triangle with the lines {a} {b} {c} is scalene')
else:
    print('Impossible!')