from cvc5_pythonic_api import *
a = String('A')
const = StringVal('hello')
solve(a == const)
b = String('B')
solve(a == a.concat(b), a == const)
solve(a == concat(a,b),b == const)
solve(a == a+const)
solve(a == const+a)
