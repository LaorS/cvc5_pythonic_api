from cvc5_pythonic_api import *
a = String('a')
b = String('b')
a_b = concat(a,b)
solve(a == a_b)

