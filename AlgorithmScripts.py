import numpy as np
import scipy as sp

class Big_matrix:
  def __init__(self, matrix):
    self.__matrix = matrix

  def get_row(self, i):
    return self.__matrix[i]

  def get_col(self, i):
    return self.__matrix[:, i]
  
  
