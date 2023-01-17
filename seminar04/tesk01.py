# 3. Создайте словарь заданный по формуле 3*n+1, где n это ключ, а формула значение
#
# *Пример:*
#
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# my_dict = {}
#
# number = int(input('Введите целое число: '))
#
# for n in range(1, number+1):
#     my_dict[n] = 3*n+1
# print(my_dict)

# Найдите корни квадратного уравнения Ax² + Bx + C = 0
# с помощью математических формул нахождения корней квадратного уравнения

# equation = '3*x**2 + 5*x - 6 = 0'
# equation = equation.replace('*x**2', '')
# equation = equation.replace('*x', '')
# equation = equation.replace('= 0', '')
# equation = equation.rstrip()
# equation = equation.split(' ')
# print(equation)
# a = int(equation[0])
# b = int(equation[2])
# c = int(equation[4])
# if equation[1] == '-':
#     b *= -1
# if equation[3] == '-':
#     c *= -1
# print(a, b, c)
# discrimenant = b ** 2 - 4 * a * c
#
# if discrimenant < 0:
#     print('Решения нет')
# elif discrimenant == 0:
#     print(-(b / (2 * a)))
# else:
#     x1 = round((-b + (discrimenant) ** 0.5) / (2 * a), 3)
#     x2 = round((-b - (discrimenant) ** 0.5) / (2 * a), 3)
#     print(f'x1 = {x1} , x2 = {x2}', )

equation = '3*x**2 + 5*x - 6 = 0'
def cobe_fnd(equation:str):
    new_equation = equation.replace(' ','').replace('=0','').replace('+',' ').replace('-',' -')
    new_equation = new_equation.split()
    new_list = []
    for item in new_equation:
        if item.startswith('x'):
            new_list.append(1)
        elif item.startswith('-x'):
            new_list.append(-1)
        else:
            new_list.append(item.split('*x')[0])
    return new_list
def solve_equation(cobe_fnd):
    a,b,c = int(cobe_fnd[0]),int(cobe_fnd[1]),int(cobe_fnd[2])
    disc = b**2 - 4 * a * c
    if disc > 0:
        x1 = round((-b + (disc) ** 0.5) / (2 * a), 3)
        x2 = round((-b - (disc) ** 0.5) / (2 * a), 3)
        return x1,x2
    elif disc == 0:
        x = round((-b - (discrimenant) ** 0.5) / (2 * a), 3)
        return x
    else:
        return None
print(solve_equation(cobe_fnd(equation)))