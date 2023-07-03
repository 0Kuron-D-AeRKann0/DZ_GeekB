n = int(input('Введите размер: '))
list_n = input('Введите значения списка через пробел: ').split()
arr = list(map(int, list_n))
x = int(input('Введите значение: '))
a = 0

for i in range(n):
    if arr[i] == x:
        a += 1
print(f'Число {x} встречается в списке А {a} раз.') 