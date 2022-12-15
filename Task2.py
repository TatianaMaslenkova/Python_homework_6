# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и 
# предпоследний и т.д.

import random
size = abs(int(input('Количество чисел в списке: ')))
init_list = [random.randint(-10, 10) for _ in range(0, size)]
print(init_list)
pr_list_len = [i for i in range((len(init_list) + 1) // 2)]
prod_list = list(map(lambda i: (init_list[i] * init_list[- i - 1]), pr_list_len))
print(prod_list)

# запрашиваем у пользователя длину списка, заполняем его случайными числами и выводим на экран
# определяем длину нового массива 
# пробегаемся по элементам изначального списка и умножаем пары чисел

# Изначальное решение:
# import random
# def fill_list(in_list: list, n: int) -> list:
#     for i in range(0, n):
#         in_list.append(random.randint(-10, 10))
#     print(in_list)

# def product_of_elements_pairs(in_list: list, n_list: list) -> list:
#     i = 0
#     while i < (len(in_list) + 1) // 2:
#         n_list.append(in_list[i] * in_list[(-i-1)])
#         i += 1
#     print(n_list)
   
# size = abs(int(input('Количество чисел в списке: ')))
# init_list = []
# new_list = []

# fill_list(init_list, size)
# print('Произведение пар чисел списка равно: ')
# product_of_elements_pairs(init_list, new_list)