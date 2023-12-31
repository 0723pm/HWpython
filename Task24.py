# В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени 
# сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать 
# за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

from random import randint
list_of_bush = list(randint(1, 100) for i in range(int(input("Введите количество кустов: "))))
print(list_of_bush)
a = int(input("Введите номер куста: "))
count = 0
if a == 1:
    count = list_of_bush[0] + list_of_bush[1] + list_of_bush[-1]
elif a == len(list_of_bush):
    count = list_of_bush[-2] + list_of_bush[-1] + list_of_bush[0]
else:
    count = list_of_bush[a-1] + list_of_bush[a-2] + list_of_bush[a]
print(count)