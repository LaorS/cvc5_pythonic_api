from cvc5_pythonic_api import *
#from z3 import *


def reset_solver(s):
    s.reset()
    s.set('produce-unsat-assumptions','true')

def check_unsat_core(assertions, core):
    slvr = Solver()
    slvr.set('produce-unsat-assumptions','true')
    for a in assertions:
        slvr.add(a)
    return s.check(*core) == unsat

nontrivial_counter = 0 

p1, p2, p3 = Bools('p1 p2 p3')
x, y = Ints('x y')
s = Solver()
s.set('produce-unsat-assumptions','true')

assertions = [Implies(p1, x > 0), Implies(p2, y > x), Implies(p2, y < 1), Implies(p3, y > -3)]

for a in assertions:
    s.add(a)

assumptions = [p1,p2,p3]

s.check(*assumptions)

core = s.unsat_core()


assert sum([c in assumptions for c in core]) == len(core)
assert check_unsat_core(assertions,core)
if len(core) < len(assumptions):
    nontrivial_counter += 1

# example 2 - booleans

reset_solver(s)

a, b, c = Bools('a b c')

# Add constraints

assertions = [Or(a, b), Or(Not(a), c), Not(c) ]
for c in assertions:
    s.add(c)


# Check satisfiability
assumptions = [a,b,c]
result = s.check(*assumptions)

unsat_core = s.unsat_core()

assert sum([c in assumptions for c in unsat_core]) == len(unsat_core)
assert check_unsat_core(assertions,assumptions)
if len(unsat_core) < len(assumptions):
    nontrivial_counter += 1

# example 3 - booleans


reset_solver(s)

a, b, c = Bools('a b c')
d = Bool('d')
# Add constraints with boolean operators
assertions = [And(a, b, Not(c)), Or(a, d), Not(And(a, d)) ]
for a in assertions:
    s.add(a)

# Check satisfiability
assumptions = [a,b,c,d]
result = s.check(*assumptions)

unsat_core = s.unsat_core()

assert sum([c in assumptions for c in unsat_core]) == len(unsat_core)
assert check_unsat_core(assertions,assumptions)
if len(unsat_core) < len(assumptions):
    nontrivial_counter += 1

# example 4 - reals



reset_solver(s)

x = Real('x')
y = Real('y')
z = Real('z')

assertions = [x + y == 5, y - z > 2, z > 3 ]
for a in assertions:
    s.add(a)

# Check satisfiability
assumptions = [x > 0, y > 0, z > 0]
result = s.check(*assumptions)

unsat_core = s.unsat_core()

assert sum([c in assumptions for c in unsat_core]) == len(unsat_core)
assert check_unsat_core(assertions,assumptions)
if len(unsat_core) < len(assumptions):
    nontrivial_counter += 1
    

# example 5 - strings


reset_solver(s)


# Define string variables
s1 = String('s1')
s2 = String('s2')

# Add string constraints
assertions = [Or(s1 == "hello", s1 == "world"), s1 + s2 == "helloworld"]
for a in assertions:
    s.add(a)

# Check satisfiability

result = s.check( Length(s2) < 2)

unsat_core = s.unsat_core()

assert sum([c in [ Length(s2) < 2 ] for c in unsat_core]) == len(unsat_core)
assert check_unsat_core(assertions,[ Length(s2) < 2 ])
if len(unsat_core) < len([ Length(s2) < 2 ]):
    nontrivial_counter += 1

# check that there is at least one nontrivial unsat core
assert nontrivial_counter >= 1

print('success')


