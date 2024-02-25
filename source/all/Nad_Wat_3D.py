import numpy as np


def nadaraya_watson_regression(X, y, x_new, h):
    # Расчет ядерной функции
    def kernel(x, xi, h):
        return np.exp(-np.linalg.norm(x - xi) ** 2 / (2 * h ** 2))

    # Инициализация весов и сумм для обновления
    weights_sum = 0
    weighted_sum = np.zeros((1, 3))

    # Проход по всем точкам данных
    for i in range(X.shape[0]):
        # Вычисление веса для i-ой точки данных
        weight = kernel(x_new, X[i], h)

        # Обновление сумм и весов
        weighted_sum += weight * y[i]
        weights_sum += weight

    return weighted_sum / weights_sum  # оценка значения в заданной точке


# Пример использования функции
X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
y = np.array([10, 20, 30])
x_new = np.array([2, 3, 4])
h = 0.5

predicted_y = nadaraya_watson_regression(X, y, x_new, h)
# print(*predicted_y)
