import numpy as np

def calculate(list): #list of 9
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")
    return

  #create the 3x3 np.array matrix
  list = np.array(list)
  arraym = list.reshape((3,3))
  
  ########################################################  
  ##for the columns
  col1 = [arraym[0][0], arraym[1][0], arraym[2][0]]
  col2 = [arraym[0][1], arraym[1][1], arraym[2][1]]
  col3 = [arraym[0][2], arraym[1][2], arraym[2][2]]
  #mean
  mean_col1 = sum(col1)/len(col1)
  mean_col2 = sum(col2)/len(col2)
  mean_col3 = sum(col3)/len(col3)
  col_mean = [mean_col1, mean_col2, mean_col3]
  #variance
  var_col1 = np.var(col1)
  var_col2 = np.var(col2)
  var_col3 = np.var(col3)
  col_var = [var_col1, var_col2, var_col3]
  #standard deviation
  std_col1 = np.std(col1)
  std_col2 = np.std(col2)
  std_col3 = np.std(col3)
  col_std = [std_col1, std_col2, std_col3]  
  #max
  max_col1 = max(col1)
  max_col2 = max(col2)
  max_col3 = max(col3)
  col_max = [max_col1, max_col2, max_col3]
  #min
  min_col1 = min(col1)
  min_col2 = min(col2)
  min_col3 = min(col3)
  col_min = [min_col1, min_col2, min_col3]
  #sum
  sum_col1 = sum(col1)
  sum_col2 = sum(col2)
  sum_col3 = sum(col3)
  col_sum = [sum_col1, sum_col2, sum_col3]
  
  ########################################################
  ##for the rows
  row1 = arraym[0]
  row2 = arraym[1]
  row3 = arraym[2]
  #mean
  mean_row1 = sum(row1)/len(row1)
  mean_row2 = sum(row2)/len(row2)
  mean_row3 = sum(row3)/len(row3)
  row_mean = [mean_row1, mean_row2, mean_row3]
  #variance
  var_row1 = np.var(row1)
  var_row2 = np.var(row2)
  var_row3 = np.var(row3)
  row_var = [var_row1, var_row2, var_row3]
  #standard deviation
  std_row1 = np.std(row1)
  std_row2 = np.std(row2)
  std_row3 = np.std(row3)
  row_std = [std_row1, std_row2, std_row3]  
  #max
  max_row1 = max(row1)
  max_row2 = max(row2)
  max_row3 = max(row3)
  row_max = [max_row1, max_row2, max_row3]
  #min
  min_row1 = min(row1)
  min_row2 = min(row2)
  min_row3 = min(row3)
  row_min = [min_row1, min_row2, min_row3]
  #sum
  sum_row1 = sum(row1)
  sum_row2 = sum(row2)
  sum_row3 = sum(row3)
  row_sum = [sum_row1, sum_row2, sum_row3]

  ########################################################
  ##for flattened matrix
  #mean
  flat_mean = sum(list)/len(list)
  #variance
  flat_var = np.var(list)
  #standard deviation
  flat_std = np.std(list)
  #max
  flat_max = max(list)
  #min
  flat_min = min(list)
  #sum
  flat_sum = sum(list)
  
  ########################################################
  ##creat the dictionary
  
  calculations = {'mean': [col_mean, row_mean, flat_mean],
                  'variance': [col_var, row_var, flat_var],
                  'standard deviation': [col_std, row_std, flat_std],
                  'max': [col_max, row_max, flat_max],
                  'min': [col_min, row_min, flat_min],
                  'sum': [col_sum, row_sum, flat_sum]}
  
  
  return calculations