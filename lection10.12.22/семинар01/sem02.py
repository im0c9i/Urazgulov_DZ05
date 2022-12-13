# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

#   Примеры:

#  - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

list = []

for i in range(5):
    list.append(int(input(f' {i+1} Введите число ')))
my_max = list[0]
for item in my_max:
    if my_max < item:
        list = my_max
    
print(my_max)