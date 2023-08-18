from sympy import Symbol, pprint, summation, init_printing, sympify
from sympy.core.sympify import SympifyError


def find_series(nth_term, N):
    """
    Prints series if nth_term and 
    number of terms is supplied.
    """
    n = Symbol('n')
    series = summation(nth_term, (n, 1, N))

    init_printing(order = 'rev-lex')
    pprint(series)

# driver program
if __name__ == "__main__":
    nth_term = input("Enter the nth term: ")
    n = input('Enter number of terms: ')
    n = int(n)
    try:
        nth_term = sympify(nth_term)
    except SympifyError:
        print('Invalid nth term')
    else:
        find_series(nth_term, n)

