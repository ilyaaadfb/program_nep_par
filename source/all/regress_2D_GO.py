from nep_2D import nep_regression_2D
from get_points import get_data2D

# get_data2D(name_file)[0] - X
# get_data2D(name_file)[1] - Y

proc = 30
name_file = f'dataXY_{proc}.txt'
x = get_data2D(name_file)[0]
y = get_data2D(name_file)[1]
nep_regression_2D(x, y)