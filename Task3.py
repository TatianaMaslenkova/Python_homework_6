# Сформировать список из N членов последовательности. Для N = 5: 1, -3, 9, -27, 81 и т.д

num = int(input('Введите число: '))
res = -3
print(list(res**(i) for i in range(0, num)))

# запрашиваем у пользователя количество членов последовательности
# пробегаемся по элементам списка степеней и поочерёдно возводим в них определённое число (в данном 
# случае, это -3) и выводим результат на экран.

# Изначальное решение:
# num = int(input('Введите число: '))
# res = 1
# for i in range(0, num):
#     print(res, end = ' ')
#     res *= -3

# for i in range(int(input())):
#     print((-3)**i, end = ' ')