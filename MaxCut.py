"""
  The problem from QHackathon:
  Given Graph[{1 <-> 2, 1 <-> 3, 2 <-> 3, 3 <-> 4, 2 <-> 5, 4 <-> 5}] # <- Wolfram code
  1) Express Cost function in terms of QUBO 
  2) Find its max value 
  3) and the cut configuration
"""
import numpy as np 

def cost_function(x):  
    Q = np.array([[2, -1, -1, 0, 0],
         [-1, 3, -1, 0, -1],
         [-1, -1, 3, -1, 0],
         [0, 0, -1, 2, -1],
         [0, -1, 0, -1, 2]])
    return np.transpose(x) @ Q @ x

solutions = []
for i in range(2**5):
    x = [int(d) for d in str(bin(i))[2:].zfill(5)]
    print('x=', x, '   cost=', cost_function(x))
    if cost_function(x) == 5:
        solutions.append(x)
print('solution = ', solutions)
