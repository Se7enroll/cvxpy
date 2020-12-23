"# cvxpy" 
Example solution to Taha Operational Analysis example 2.3-2 with CVXPY.
The constraints are verbatim the example, but should be rewritten in matrix form.

>>> print(f"Function value: {result}")
Function value: 5.090322814811609
>>> print(f"Solution: \n{x.value}")
Solution:
[[  5.09    3.1     0.      0.      5.   ]
 [  1.26    5.737   1.262   0.      3.   ]
 [  3.5     1.958   5.737   0.      0.607]
 [100.    100.    100.      5.737  46.724]
 [  0.      0.      2.415   1.11    5.737]]