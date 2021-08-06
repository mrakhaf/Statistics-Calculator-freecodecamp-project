import numpy as np

def calculate(list):
  if len(list)!=9:
    raise ValueError('List must contain nine numbers.')
  list_matrix = np.array(list).reshape(3,3)  
  list_matrix_mean = [list_matrix.mean(axis=0).tolist(), list_matrix.mean(axis=1).tolist(), list_matrix.mean()]
  list_matrix_variance = [list_matrix.var(axis=0).tolist(), list_matrix.var(axis=1).tolist(), list_matrix.var()]
  list_matrix_stdev = [list_matrix.std(axis=0).tolist(), list_matrix.std(axis=1).tolist(), list_matrix.std()]
  list_matrix_min = [list_matrix.min(axis=0).tolist(), list_matrix.min(axis=1).tolist(), list_matrix.min()]
  list_matrix_max = [list_matrix.max(axis=0).tolist(), list_matrix.max(axis=1).tolist(), list_matrix.max()]
  list_matrix_sum = [list_matrix.sum(axis=0).tolist(), list_matrix.sum(axis=1).tolist(), list_matrix.sum()]

  calculations = {
    'mean': list_matrix_mean,
    'variance': list_matrix_variance,
    'standard deviation': list_matrix_stdev,
    'max': list_matrix_max,
    'min': list_matrix_min,
    'sum': list_matrix_sum
  }

  
  return calculations

  