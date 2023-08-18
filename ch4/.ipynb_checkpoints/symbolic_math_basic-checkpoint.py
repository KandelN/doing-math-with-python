# Single variable
from sympy import Symbol
x = Symbol('x')
a = x
print(x)
print(a)
print(x.name)
print(x*x*x)
print(x+x)

# Multiple variables
from sympy import symbols
p, q, r = symbols('p, q, r')
expr = p*2 + p + q**2 + p*q*r*3 + 17 + q*q
print('\nf(p, q, r) =', expr)

# Substitution
res = expr.subs({
    p:1,
    q:2,
    r:0
    })
print("f(1,2,0) =",res)

# Variable susbtitution
expr_ii = expr.subs({
    r: p,
    q:1/p
})
print("if r = p:")
print("\tf(p,q,r) =", expr_ii)

# Converting strings into math expression
# SympifyError
from sympy import sympify
from sympy.core.sympify import SympifyError
expr = input("Enter a  mathematical expression: ")
try:
    expr = sympify(expr)
except SympifyError:
    print("Invalid Input")
else:

    # preety printing
    from sympy import pprint
    pprint(expr)

