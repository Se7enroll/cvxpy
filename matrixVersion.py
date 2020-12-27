import numpy as np
import cvxpy as cp

# printing options
np.set_printoptions(precision=5)
np.set_printoptions(suppress=True)

# define rates
rates = np.array([1.0, .769, .625, 105.0, .342])
n = len(rates)

#setup problem in cvxpy terms
x = cp.Variable([n,n])

# maximize dollar y which is first entry in x
objective = cp.Maximize(x[0,0]) 

# helper matrix ratemat is currency table in taha page 33
# note that the diagonal of ratemat is 1
ratemat = np.array([ (rates/rates[i])**(-1) for i in range(n) ])

# Constraints
# the constraints from the book can be expressed as the row sum minus the col sum
# times the inverse rate expressed in basis of each of the currencys:
constraints = [
    cp.sum(x[0,:]) - ratemat[0,:] @ x[:,0] + x[0,0] == 5,
    cp.sum(x[1,:]) - ratemat[1,:] @ x[:,1] == 0,
    cp.sum(x[2,:]) - ratemat[2,:] @ x[:,2] == 0,
    cp.sum(x[3,:]) - ratemat[3,:] @ x[:,3] == 0,
    cp.sum(x[4,:]) - ratemat[4,:] @ x[:,4] == 0,
    # bounds
    x >= 0,
    x[0,1:4] <= 5,
    x[1,[0,2,3,4]] <= 3,
    x[2,[0,1,3,4]] <= 3.5,   
    x[3,[0,1,2,4]] <= 100,
    x[4,0:4] <= 2.8,
    
]

# define problem and solve
p = cp.Problem(objective, constraints)
result = p.solve()
print(f"Function value: {result}")
print(f"Solution: \n{x.value}")

# We see that the "arbitrage" that the problem exihibits in the book, is purely due to rounding errors, 
# so entering the ratematrix as in the book:

ratematverbatim = np.array([
    [1.0, 1/.769, 1/.625, 1/105, 1/.342],
    [.769, 1.0,  1/.813, 1/137, 1/.445],
    [.625, .813, 1.0,  1/169, 1/.543],
    [105.0, 137.0, 169.0, 1.0, 1/.0032],
    [.342, .445, .543, .0032, 1.0]
])

# in the constraints we again must limmit the precision, so the matrix multiplication is done elementwise
# with rounding imposed:

constraints2 = [
    cp.sum(x[0,:]) - ratematverbatim[0,:] @ x[:,0] + x[0,0] == 5,
    cp.sum(x[1,:]) - ratematverbatim[1,:] @ x[:,1] == 0,
    cp.sum(x[2,:]) - ratematverbatim[2,:] @ x[:,2] == 0,
    cp.sum(x[3,:]) - ratematverbatim[3,:] @ x[:,3] == 0,
    cp.sum(x[4,:]) - ratematverbatim[4,:] @ x[:,4] == 0,
    # bounds
    x >= 0,
    x[0,1:4] <= 5,
    x[1,[0,2,3,4]] <= 3,
    x[2,[0,1,3,4]] <= 3.5,   
    x[3,[0,1,2,4]] <= 100,
    x[4,0:4] <= 2.8,
    
]

# solve againt - now with the same result as the book (within 0.3 % atleast...):
p2 = cp.Problem(objective, constraints2)
result2 = p2.solve()
print(f"Function value: {result2}")
print(f"Solution: \n{x.value}")