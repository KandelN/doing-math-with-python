from sympy import sympify, Symbol, solve
from sympy.plotting import plot
from sympy.core.sympify import SympifyError

def find_roots(ex1, ex2):
    """
    Prints solutions of two expression.
    """
    roots = solve((ex1, ex2), dict = "True")
    print("Solving i and ii:")
    for root in roots:
        print(root)
    
def plot_expression(expr1, expr2):
    """
    Solves two expression and plots them.
    """
    # standarize expressions
    y = Symbol('y')
    expr_y_1 = solve(expr1, y)[0]
    expr_y_2 = solve(expr2, y)[0]
    
    # Solve expressions
    find_roots(expr1, expr2)

    # Plot expressions
    p = plot(expr_y_1, expr_y_2, legend = True,
        xlabel="x", ylabel = "y", show = False)
    p[0].line_color = 'r'
    p[1].line_color = 'b'
    p.save('graphical_solver.png')

# driver program
if __name__ == "__main__":
    expr1 = input("Enter first expression in terms of x and y: ")    
    expr2 = input("Enter second expression in terms of x and y: ")    
    try:
        expr1 = sympify(expr1)
        expr2 = sympify(expr2)
    except SympifyError:
        print("Invalid Expression")
    else:
        plot_expression(expr1, expr2)
