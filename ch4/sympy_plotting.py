from sympy import Symbol
from sympy.plotting import plot

x = Symbol('x')
p = plot((2*x + 3), (x, -5, 5),
    title = "line", xlabel="x", ylabel = "2x+3", show = False)
p.save('line.png')

