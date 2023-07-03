n = int(input('Введите размер: '))
list_n = input('Введите элементы списка через пробел: ').split()
arr = list(map(int, list_n))
x = input('Введите значения: ')
z = 0


for i in range(n):
    if arr[i] == x:
        z += 1
print(f'Ваше число ближе всего к {z}')