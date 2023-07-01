# x = int(input('Введите число X: '))
# y = int(input('Введите число Y: '))

# for a in range(x):
#     for b in range(y):
#         if x == a + b and y == a * b:
#             print(a,b)

x = int(input())
y = int(input())
for i in range(x):
    for j in range(y):
        if x == i + j and y == i * j:
            print(i, j)