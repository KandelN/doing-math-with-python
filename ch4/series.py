import sys
from sympy import Symbol, pprint, init_printing

def print_series(n):

    # initialize settings and variables
    init_printing(order = 'rev-lex')
    x = Symbol('x') 
    series = 0

    for i in range(1, n+1, 1):
        series += x**i / i
    
    pprint(series)
    
    print( series.subs({x:float( input( "\nEnter a value for x: " ) ) }) )


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python series.py [n]")
    n  = int( sys.argv[1] )
    print_series(n)
    
