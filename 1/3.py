name = input('enter the name->>')
age = int(input('enter the age->>'))
if age >= 16:
    print('Поздравляем вы поступили во ВГУИТ')
if age < 16:
    print("Сначала нужно окончить школу")
if 0 < age < 75:
    print("возраст подходит")
if name != 'Иван':
    print('Поступающего зовут не Иван')