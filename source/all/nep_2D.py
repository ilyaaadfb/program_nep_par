# импортируем необходимые модули
import matplotlib.pyplot as plt
import numpy as np


# from Nad_Wat import nonparametric
import plotly.graph_objs as go
# from Nad_Wat import bell_shaped_kernel_parabola
from get_points import get_data2D


# колоколообразная ядерная функция
def bell_shaped_kernel_parabola(p):
    if p ** 2 <= 5:
        return 0.335 - 0.067 * p ** 2
    else:
        return 0


# функция для вычисления значения по формуле Надарая-Ватсона
def nonparametric(x_dop, c, xi_list, yi_list):
    numerator = 0
    denominator = 0

    for i in range(len(xi_list)):  # вычисление весов точек
        phi_value = bell_shaped_kernel_parabola((x_dop - xi_list[i]) / c)
        numerator += yi_list[i] * phi_value
        denominator += phi_value
    if denominator != 0:
        return numerator / denominator  # оценка значения в заданной точке
    return 0


# функция для вычисления модельного y
def nonparametric_for_e(x_dop, c, x, y):
    s1, s2 = 0, 0
    for i in range(len(y)):
        mu = 1 if x_dop != x[i] else 0
        s1 += y[i] * bell_shaped_kernel_parabola((x_dop - x[i]) / c) * mu
        s2 += bell_shaped_kernel_parabola((x_dop - x[i]) / c) * mu
    if s2 != 0:
        return s1 / s2
    return 0


# функция для вычисления ошибки
def E(x, y, c):
    e = 0
    for i in range(len(x)):
        ym = nonparametric_for_e(x[i], c, x, y)
        e += (y[i] - ym) ** 2
    return (e / len(x)) ** 0.5


# функция выполняющая непараметричскую регрессию
def nep(x, y):
    e_lst = []
    c_lst = []
    c_best, e_best = None, None
    for c in np.arange(0.001, 5, 0.01):
        c_lst.append(c)
        e = E(x, y, c)
        e_lst.append(e)
        if e_best is None or e < e_best:
            e_best, c_best = e, c

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=c_lst, y=e_lst, name='$$Поведение ошибки$$',
                             marker=dict(color='red', size=3)))
    fig.update_layout(xaxis_title="e", yaxis_title="c")
    fig.show()

    x_nep = []
    y_nep = []
    for x_dop in np.arange(min(x), max(x), 0.1):
        y_dop = nonparametric(x_dop, c_best, x, y)
        x_nep.append(x_dop)
        y_nep.append(y_dop)

    # # График
    # fig = go.Figure()
    # fig.add_trace(go.Scatter(x=x, y=y, mode='markers', name='$$Исходные данные$$',
    #                          marker=dict(color='green')))
    # fig.add_trace(go.Scatter(x=x_nep, y=y_nep, name='$$Непараметрическая регрессия$$',
    #                          marker=dict(color='blue')))
    # fig.add_trace(
    #     go.Scatter(x=x_nep, y=y_nep, mode='markers', name='$$Точки непараметрической регрессии$$',
    #                marker=dict(color='red', symbol="star-triangle-up")))
    # fig.update_layout(xaxis_title="X", yaxis_title="Y")
    # fig.show()

    # plt.scatter(x, y, color='red', s=15)  # точки
    # plt.xlim([min(x) - 2, max(x) + 2])
    # plt.ylim([min(y) - 2, max(y) + 2])
    # plt.xlabel('x')
    # plt.ylabel('y')
    # plt.plot(x_nep, y_nep, color='brown', label="Непараметрическая регрессия")
    # plt.legend(loc='best')

proc = 30
name_file = f'dataXY_{proc}.txt'
x = get_data2D(name_file)[0]
y = get_data2D(name_file)[1]

nep(x, y)
