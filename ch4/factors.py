from sympy import sympify, factor, simplify
from sympy.core.sympify import SympifyError

if __name__ == "__main__":
    expr = input("Enter valid mathematical expression: ")
    try:
        expr  = sympify(expr)
    except SympifyError:
        raise SympifyError("Invalid Expression")
    else:
        factored =factor(expr) 
        print(factored)



        