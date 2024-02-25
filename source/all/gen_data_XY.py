# импортируем необходимые модули
import numpy as np
import random

# сгенерируем 100 случайных точек где Y - синус X
X = np.linspace(-10, 10, 100)
Y = np.sin(X)

# пройдёмся циклом по коэффициентам процентов
for proc in range(0, 160, 10):
    # процент шума = proc
    # добавим шум в данные по формуле
    Y2 = [Yi + random.uniform(-(((max(Y) - min(Y)) * proc / 100) / 2),
                              (((max(Y) - min(Y)) * proc / 100) / 2)) for Yi in Y]
    data = np.array([X, Y2]).T
    # добавим данные в файл, в название укажем процент шума
    with open(f'dataXY_{round(proc)}.txt', 'w') as f:
        [print(i, j, file=f) for i, j, in data]




