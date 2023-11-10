"""
  The problem from QHackathon:
  Given Graph[{1 <-> 2, 1 <-> 3, 2 <-> 3, 3 <-> 4, 2 <-> 5, 4 <-> 5}] # <- Wolfram code
  1) Express Cost function in terms of QUBO 
  2) Find its max value 
  3) and the cut configuration
"""
import numpy as np 

def QUBO_matrix(G, N_edges):
    """
    From graph G written in the form [(i,j),...]
    create matrix for QUBO formulation
    """
    Q = np.zeros((N_edges, N_edges))
    for g in G:
        i,j = g[0], g[1]
        Q[i-1,i-1]+= 1
        Q[j-1,j-1]+= 1
        Q[i-1,j-1]+= -1
        Q[j-1,i-1]+= -1
    return Q

def cost_function(x, Q):  
    """
    Given binary variable x_i associated with every vertex of a graph,  
    x is binary vector with components x_i 
    Q is QUBO-matrix of size len(x)
    returns cost function
    """
    return np.transpose(x) @ Q @ x
#######################################################################
N_edges = 5 # number of edges
G = [(1,2),(1,3),(2,5),(2,3),(3,4),(4,5)] # graph

Q = QUBO_matrix(G, N_edges)
# verify QUBO matrix
print(Q == np.array([[2, -1, -1, 0, 0],
         [-1, 3, -1, 0, -1],
         [-1, -1, 3, -1, 0],
         [0, 0, -1, 2, -1],
         [0, -1, 0, -1, 2]]))
print()
solutions = []
# brute force solution: loop over binary numbers from' 00000' to '11111'
for i in range(2**N_edges): 
    x = [int(d) for d in str(bin(i))[2:].zfill(N_edges)]
    print('x=', x, '   cost=', cost_function(x,Q))
    if cost_function(x, Q) == 5: # max cost value is 5 
        solutions.append(x)
print()
print('solution = ', solutions)
