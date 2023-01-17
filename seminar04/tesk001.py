equation = '3*x**2 + 5*x - 6 = 0'
def cobe_fnd(equation:str):
    new_equation = equation.replace(' ','').replace('=0','').replace('+','').replace('-',' -')
    new_equation = new_equation.split()
    print(new_equation)
