# Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) 
# на K элементов вправо,  K – положительное число.
# Input:   [1, 2, 3, 4, 5] k = 3
# Output:  [3, 4, 5, 1, 2]
# Примечание: Пользователь может вводить значения списка или список задан изначально.

from random import randint as rd
# as(alias) - псевдоним


n = int(input("Введите кол-во элементов: "))
numbers = list() # []
for i in range(n):
    numbers.append(rd(1, 51)) # [1; 50]
print(numbers)
k = int(input("Введите кол-во элементов для сдвига: "))
k = k % n

# [1, 2, 3, 4, 5] k = 3
#  0  1  2  3  4
# [3, 4, 5, 1, 2]
#  2  3  4  0  1
result = [0] * n
for i in range(k): # 0 1 2
    result[i] = numbers[n - k + i]
for i in range(n - k):
    result[k + i] = numbers[i]
print(result)