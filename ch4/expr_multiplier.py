from sympy import sympify, expand, pprint
from sympy.core.sympify import SympifyError

if __name__ == "__main__":
    expr1 = input("Enter first expression:")
    expr2 = input("Enter second expression:")

    try:
        expr1 = sympify(expr1)
        expr2 = sympify(expr2)
    except SympifyError:
        print("Invalid expression")
    else:
        prod = expand(expr1*expr2)
        print(prod)