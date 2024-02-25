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


