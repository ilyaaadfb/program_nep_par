import numpy as np
import matplotlib.pyplot as plt
from Nad_Wat import nonparametric
from get_points import get_data2D
from Nad_Wat import bell_shaped_kernel_parabola
proc = 30
name_file = f'dataXY_{proc}.txt'
x = get_data2D(name_file)[0]
y = get_data2D(name_file)[1]

def nonparametric_for_e(x_dop, c, x, y):
    s1, s2 = 0, 0
    for i in range(len(y)):
        mu = 1 if x_dop != x[i] else 0
        s1 += y[i] * bell_shaped_kernel_parabola((x_dop - x[i]) / c)*mu
        s2 += bell_shaped_kernel_parabola((x_dop - x[i]) / c) * mu
    if s2 != 0:
        return s1 / s2
    return 0

def E(x, y, c):
    e = 0
    for i in range(len(x)):
        ym = nonparametric_for_e(x[i], c, x, y)
        e += (y[i] - ym)**2
    return (e/len(x))**0.5

# def C_best():
c_lst = []
e_lst = []
c_best = None
e_best = None
for c in np.arange(0.001, 5, 0.01):
    c_lst.append(c)
    e = E(x, y, c)
    e_lst.append(e)
    if e_best is None or e < e_best:
        e_best = e
        c_best = c

print(c_best)
fig, ax = plt.subplots()
plt.plot(c_lst, e_lst)
plt.show()