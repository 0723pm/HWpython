# Дан массив, состоящий из целых чисел. 
# Напишите программу, которая подсчитает количество элементов массива, 
# больших предыдущего (элемента с предыдущим номером) 
# Input: [0, -1, 5, 2, 3]
# Output: 2 
# Пояснение: (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения списка или список задан изначально.

from random import randint as rd


n = int(input("Введите кол-во элементов: "))
numbers = list() # []
count = 0
for i in range(n):
    numbers.append(rd(1, 21))
print(numbers)
for i in range(1, n):
    if numbers[i] > numbers[i - 1]:
        count += 1
print(count)