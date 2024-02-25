# импортируем необходимые модули
import numpy as np
from scipy.optimize import curve_fit
import plotly.graph_objs as go


# создадим функцию для аппроксимации на вход которой
# подаются три массива X и Y и Z
def approx_3D(x, y, z):
    x = np.array(list(map(float, x)))
    y = np.array(list(map(float, y)))
    z = np.array(list(map(lambda x: x/10, z)))
    # Определение математической функции для
    # аппроксимации кривой
    def func(xy, a):
        x, y = xy
        return a * np.sin(x)
    # Выполнить подгонку кривой
    popt, pcov = curve_fit(func, (x, y), z)
    # Функция для реализации 3D-графика точек данных
    # и подобранной кривой
    x_range = np.linspace(-10, 10, 100)
    y_range = np.linspace(-10, 10, 100)
    X, Y = np.meshgrid(x_range, y_range)
    Z = func((X, Y), *popt)
    fig = go.Figure()
    fig.add_trace(go.Scatter3d(x=x, y=y, z=z, mode='markers', marker=dict(color='blue', size=2)))
    fig.add_trace(go.Surface(x=X, y=Y, z=Z, colorscale='Reds', opacity=0.5))
    fig.update_layout(scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z'
    ))
    fig.show()
