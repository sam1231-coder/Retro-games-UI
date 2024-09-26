import pandas as pd
dataset = pd.dataframe({ 'id':[101,102,103,104,105,106,107],
'salary':[120000,145000,320000,45000,90000,134000,200000]})

def min_max_scaling(column):
            min_value = column.min()
            max_value = column.max()
            scaled_column = (column - min_value)/ (max_value - min_value)
            return scaled_column

scaled_salary=min_max_scaling(salary)
print(dataset)
