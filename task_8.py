year = int(input('Введите год'))
if year % 4 != 0:
    print("обычный год")
elif year % 100 == 0:
    if year % 400 == 0:
        print('Высокосный год')
    else:
        print('Обычный год')
else:
    print('Высокосный год')
