from sympy import Symbol, symbols, solve

x = Symbol('x')
a, b, c = symbols('a,b,c')

expr = a*x**2 + b*x + c
roots = solve(expr, x, dict = True)

print(roots)
