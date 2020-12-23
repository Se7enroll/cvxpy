import numpy as np
import cvxpy as cp

# printing options
np.set_printoptions(precision=3)
np.set_printoptions(suppress=True)

#setup problem in cvxpy terms
x = cp.Variable([n,n])

# maximize dollar y
objective = cp.Maximize(x[0,0])     

constraints = [
    x[0,0] + x[0,1] + x[0,2] + x[0,3] + x[0,4] - 1/.769*x[1,0] - 1/.625*x[2,0] - 1/105*x[3,0] - 1/.342*x[4,0] == 5,
    
    x[1,0] + x[1,2] + x[1,3] + x[1,4] - .769*x[0,1] - 1/.813*x[2,1] - 1/137*x[3,1] - 1/.445*x[4,1] == 0,
    
    x[2,0] + x[2,1] + x[2,3] + x[2,4] - .625*x[0,2] - .813*x[1,2] - 1/169*x[3,2] - 1/.543*x[4,2] == 0,

    x[3,0] + x[3,1] + x[3,2] + x[3,4] - 105*x[0,3] - 137*x[1,3] - 169*x[2,3] - 1/.0032*x[4,3] == 0,
    
    x[4,0] + x[4,1] + x[4,2] + x[4,3] - .342*x[0,4] - .445*x[1,4] - .543*x[2,4] - .0032*x[3,4] == 0,
    
    # add transaction limits:
    x >= 0,
    x[0,1] <= 5,
    x[0,2] <= 5,
    x[0,3] <= 5,
    x[0,4] <= 5,

    x[1,0] <= 3,
    x[1,2] <= 3,
    x[1,3] <= 3,
    x[1,4] <= 3,

    x[2,0] <= 3.5,
    x[2,1] <= 3.5,
    x[2,3] <= 3.5,
    x[2,4] <= 3.5,
    
    x[3,0] <= 100,
    x[3,1] <= 100,
    x[3,2] <= 100,
    x[3,4] <= 100,

    x[4,0] <= 2.8,
    x[4,1] <= 2.8,
    x[4,2] <= 2.8,
    x[4,3] <= 2.8
]



# define problem and solve
p = cp.Problem(objective, constraints)
result = p.solve()
print(f"Function value: {result}")
print(f"Solution: \n{x.value}")
