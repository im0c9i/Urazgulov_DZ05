#number = int(input('Введите число'))
#for i in range(number):
#   print((-3)**i, end=', ')
#создать список, длиной N, значение формируется по формуле 3k+1, где к - принимает от 1 до Н.

# num_list = []
# n = int(input('Введите длину списка '))
#
# for k in range(1,n+1):
#     num_list.append(abs(3*k+1))
# print(num_list)

# Напишите программу который пользователь будет задавать две строки,
# программа - определять вхождение одной строки в другую

# stroka = str(input('Введите строку: '))
# count = stroka.count(str(input('Введите что нужно подсчитать')))
# print(count)
m = len('0.12345')
n = int(0.12345*10**(m-2))
print(n)