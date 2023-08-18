# Factoring and Expanding algebric expression
from sympy import symbols, factor, expand, pprint

def sample(expr):
    print(expr)

    expr2 = factor(expr)
    print(expr2)

    expr3 = expand(expr2)
    print(expr3)
    pprint(expr3)
    print("===================")

x, y = symbols('x,y')

expr_i = x**2 - y**2
sample(expr_i)

expr_ii = x**3 + 3*x**2*y + 3*x*y**2 + y**3
sample(expr_ii)