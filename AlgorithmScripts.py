import numpy as np
import scipy as sp

class Big_matrix:
  def __init__(self, matrix):
    self.__matrix = matrix

  def get_row(self, i):
    return self.__matrix[i]

  def get_col(self, i):
    return self.__matrix[:, i]
  
def basis(d : int, i : int):
  return np.array([1.0 if index==i else 0.0 for index in range(d)])
  
# This is one way to generate a problem, Idk if its the best way to make these 
# problems (our choice of how to do this matters)
def generate_problem(d: int, k: int):
  """
  Returns a eigenvector phase retrieval problem:
    - a Big_matrix instance
    - an eigenvalue of the instance
    - the absolute value of the entries of the eigenvector of that eigenvalue
  """
  #d is size of matrix, k is which eigenvector we want from the array of eigenvectors
  #in our model, this is harder when k is closer to d/2, k = 0 or k = d is easiest
  assert k < d
  #not <= bc of 0 indexing
  rng = np.random.default_rng(seed=1234)

  A = rng.normal(size=(d, d))
  S = A + A.T

  #S.T = A.T + A = S
  #this way eigenvalues are real
  #so now S is symmetric

  big_matrix = Big_matrix(S)
  w, V = np.linalg.eig(S)
  v_abs = np.abs(V[:, k])
  ell = w[k]
  epsilon = np.sign(V[:, k])

  B = S - ell * np.eye(d)

  return big_matrix, ell, v_abs, epsilon


  
