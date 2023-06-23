# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

from random import randint as rd
n = int(input("Введите кол-во элементов: "))
numbers = list() 
count = 0
for i in range(n):
    numbers.append(rd(1, 21))
print(numbers)
m = int(input("Введите число, которое необходимо найти: "))
count = 0
for i in range(n):
    if numbers[i] == m:
        count += 1
print(count)