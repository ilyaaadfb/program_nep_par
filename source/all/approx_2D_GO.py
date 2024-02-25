from approx_2D import approx_2D
from get_points import get_data2D

# get_data2D(name_file)[0] - X
# get_data2D(name_file)[1] - Y

proc = 120
name_file = f'dataXY_{proc}.txt'
x = get_data2D(name_file)[0]
y = get_data2D(name_file)[1]
approx_2D(x, y)