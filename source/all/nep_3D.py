# импортируем необходимые модули
import numpy as np
import plotly.graph_objs as go


# Функция для вычисления оценки Надарая-Ватсона
def nadaraya_watson(X, Z, x_query, h):
    weights = np.exp(-np.sum((X - x_query) ** 2, axis=1) / (2 * h ** 2))
    weighted_sum = np.sum(weights * Z)
    sum_of_weights = np.sum(weights)
    return weighted_sum / sum_of_weights


# функция для построения непараметрической регрессии
def nep_regression_3D(x, y, z):
    X = np.array([x, y, z]).T
    # Задание сетки для построения непараметрической регрессии по координате Z
    grid_size = 0.1
    x_range = np.arange(-10, 10, grid_size)
    y_range = np.arange(-10, 10, grid_size)
    X_grid, Y_grid = np.meshgrid(x_range, y_range)
    Z_grid = np.zeros_like(X_grid)
    # Вычисление значений по координате с помощью оценки регрессии Надарая-Ватсон
    for i in range(X_grid.shape[0]):
        for j in range(X_grid.shape[1]):
            x_query = [X_grid[i, j], Y_grid[i, j], 0]  # Поиск координаты по Z
            Z_grid[i, j] = nadaraya_watson(X, np.array(z), np.array(x_query),
                                           h=0.5)  # Вычисление значения на поверхности
    # Построение графика в 3D
    fig = go.Figure()
    fig.add_trace(go.Scatter3d(x=x, y=y, z=z, mode='markers', marker=dict(color='blue', size=2), name='Исходные данные'))
    fig.add_trace(
        go.Surface(x=X_grid, y=Y_grid, z=Z_grid, colorscale='blackbody', opacity=0.3, name='Регрессия Надарая-Ватсон'))
    fig.update_layout(scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'),
                      legend=dict(x=0, y=1, traceorder='normal'))
    fig.show()
