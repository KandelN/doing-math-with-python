from sympy import symbols, solve

x, y = symbols('x,y')
expr1 = 2*x + 3*y - 6
expr2 = 3*x + 2*y - 12
expr1 = y - 5
expr2 = 3*x + 2 - y

roots = solve((expr1, expr2), dict = True )
roots = roots[0]
print(roots)

# Check the answer
print( expr1.subs(roots))
print( expr2.subs(roots))

