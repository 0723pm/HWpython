# Определить индексы элементов массива (списка), значения которых принадлежат заданному 
# диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)


list_1=[-5, 10, 16, 4, 0, 5, 2, -10, -17, 2, -19, 4, 7]
list_2 = []
max = int(input("Введите максимум: "))
min = int(input("Введите минимум: "))
for i in range(len(list_1)):
    if list_1[i] >= min and list_1[i] <= max:
        list_2.append(i)
print(list_2)

