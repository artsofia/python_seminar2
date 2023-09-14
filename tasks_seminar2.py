# Task 10
num = int(input("Введите кол-во монеток: "))
eagle = 0
tails = 0

for i in range(num):
    coin = int(input("Введите 0 - орел или 1 - решка: "))

    if coin == 0:
        eagle += 1
    else:
        tails += 1

if eagle >= tails:
    print(tails)
else:
    print(eagle)


# Task 12
s = int(input("Введите сумму чисел: "))
p = int(input("Введите произведение чисел: "))

for x in range(s + 1):
    for y in range(p + 1):
        if (x + y == s) and (x * y == s):
            print(x, y)


# Task 14
n = int(input("Введите число: "))

for i in range(n):
    i = 2 ** i

    if i < n:
        print(i, end=" ")