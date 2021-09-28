znak = input('''
Выбирите знак:
+ Плюс
- Минус
* Умножить
/ Разделить
''')
number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))
print('{} + {} = '.format(number_1, number_2))
print(number_1 + number_2)
print('{} - {} = '.format(number_1, number_2))
print(number_1 - number_2)
print('{} * {} = '.format(number_1, number_2))
print(number_1 * number_2)
print('{} / {} = '.format(number_1, number_2))
print(number_1 / number_2)

