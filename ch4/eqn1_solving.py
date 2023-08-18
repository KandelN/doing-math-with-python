from sympy import Symbol, solve

def solve_eqn(expr):
    """
    Returns roots of expression = 0
    """
    print("\n", expr, "= 0")
    x_values = solve(expr, dict = True)
    print(x_values)

x = Symbol('x')
solve_eqn(x - 5- x - 2*x - 7)
solve_eqn(x**2 -3*x + 2)
solve_eqn(x**2 + x + 1)
