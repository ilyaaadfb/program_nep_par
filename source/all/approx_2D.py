# импортируем необходимые модули
import numpy as np
from scipy.optimize import curve_fit
import plotly.graph_objs as go
from RMSE import rmse


# создадим функцию для аппроксимации на вход
# которой подаются два массива x и y
def approx_2D(x, y):
    # Определим математическую функцию, которая
    # будет использоваться для подгонки кривой.
    # В этом примере мы будем использовать
    # синусоидальную функцию.
    def func(x, a):
        return a + np.sin(x)

    x = np.array(list(map(float, x)))
    y = np.array(list(map(float, y)))
    popt, _ = curve_fit(func, x, y)
    x_approx = np.linspace(x.min(), x.max(), 100)
    y_approx = func(x, *popt)
    return x_approx, y_approx
    # fig = go.Figure()
    # fig.add_trace(go.Scatter(x=x, y=y, mode='markers', name='$$Исходные данные$$',
    #                          marker=dict(color='green')))
    # fig.add_trace(go.Scatter(x=x_approx, y=y_approx, name='$$Синусоидальная функция$$',
    #                          marker=dict(color='blue')))
    # fig.add_trace(go.Scatter(x=x, y=func(x, *popt), mode='markers', name='$$Точки аппроксимации$$',
    #                          marker=dict(color='red', symbol="star-triangle-up")))
    # fig.update_layout(xaxis_title="X", yaxis_title="Y")
    # fig.show()
