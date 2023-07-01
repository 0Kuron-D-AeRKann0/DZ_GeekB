n = int(input('Введите число монеток: '))

Orel = 0
Reshka = 0

for i in range(n):
    x = int(input('Орел(0) или Решка(1): '))
    if x == 0:
        Orel = Orel + 1
    else: Reshka = Reshka + 1
if Orel > Reshka:
    print(f'Переверните {Reshka} монет с решки на орла')
else: print(f'Переверните {Orel} монет с орла на решку')