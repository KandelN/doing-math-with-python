from sympy import sympify, Symbol, solve
from sympy.plotting import plot
from sympy.core.sympify import SympifyError

def plot_expression(expr):

    y = Symbol('y')
    solutions = solve(expr, y)
    expr_y = solutions[0]
    print(type(expr))
    p = plot(expr_y ,
        title = f'{expr}', xlabel="x", ylabel = "y", show = False)
    p.save('plotter.png')

if __name__ == "__main__":
    expr = input("Enter the expression in terms of x and y: ")    
    try:
        expr = sympify(expr)
        print(type(expr))
    except SympifyError:
        print("Invalid Expression")
    else:
        plot_expression(expr)

        