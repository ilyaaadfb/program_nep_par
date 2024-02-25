import numpy as np
import matplotlib.pyplot as plt
from get_points import get_data3D


def bell_shaped_kernel_parabola(p):
    if p ** 2 <= 5: return 0.335 - 0.067 * p ** 2
    return 0


def nonparametric_regression_3d(x_dop1, x_dop2, x1, x2, y, c1, c2):
    numerator, denominator = 0, 0

    for i in range(len(x1)):
        numerator += y[i] * bell_shaped_kernel_parabola((x_dop1 - x1[i]) / c1) * bell_shaped_kernel_parabola(
            (x_dop2 - x2[i]) / c2)
        denominator += bell_shaped_kernel_parabola((x_dop1 - x1[i]) / c1) * bell_shaped_kernel_parabola(
            (x_dop2 - x2[i]) / c2)

    return numerator / denominator

# proc = 0
# name_file = f'dataXYZ_{proc}.txt'
# x1 = get_data3D(name_file)[0]
# x2 = get_data3D(name_file)[1]
# y = get_data3D(name_file)[2]
#
# c1 = 1
# c2 = 1
# y_new = []
# for i in range(len(x1)):
#     res = nonparametric_regression_3d(x1[i], x2[i], x1, x2, y, c1, c2)
#     y_new.append(res)
#
# # for x_dop in np.arange(min(x1), max(x1), 0.1):
# #     y_dop = nonparametric(x_dop, c_best, x, y)
# #     x_nep.append(x_dop)
# #     y_nep.append(y_dop)
#
# # Построение графика
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(x1, x2, y, color='blue', label='Исходные данные')
# ax.scatter(x1, x2, y_new, color='red', label='Полученные данные')
# ax.set_xlabel('X1')
# ax.set_ylabel('X2')
# ax.set_zlabel('Y')
# plt.legend()
# plt.show()
