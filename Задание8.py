n,m,k = int(input('Размер одной стороны шоколадки: ')),int(input('Размер другой стороны шоколадки: ')),int(input('Количесвто долек: '))

if k % n or k % m:
    print('Yes')
else: print('No')