from z3 import *

square = Int('square')
triangle = Int('triangle')
circle = Int('circle')

solver = Solver()

# constraints
solver.add(square * square * circle == 16)
solver.add(triangle * triangle * triangle == 27)
solver.add(triangle * square == 6)

# dirty way to see the result
# solver.check()
# print(solver.model())
# [square = 2, circle = 4, triangle = 3]

# find solutions and calculate new result
if solver.check() == sat:
    model = solver.model()

    # convert values to int
    circle_val = model.eval(circle).as_long()
    triangle_val = model.eval(triangle).as_long()
    square_val = model.eval(square).as_long()
    print("circle =", circle_val, ", triangle =", triangle_val, ", square =", square_val)
    result = circle_val * triangle_val * square_val
    print("result =", result)
else:
    print("No solution")