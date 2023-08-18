from sympy import symbols, solve, pprint

s, u, a, t = symbols('s,u,a,t')
expr = u*t + (1/2)*a*t**2 - s
t_expr = solve(expr, t, dict=True)
pprint(t_expr)
