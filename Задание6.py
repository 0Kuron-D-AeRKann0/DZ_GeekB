x = input('Введите номер билета: ')

a = int(x[0]) + int(x[1]) + int(x[2])
b = int(x[3]) + int(x[4]) + int(x[5])
if a == b:
    print('У вас счастливый билет')
else: print('У вас обычный билет')