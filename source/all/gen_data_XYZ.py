# импортируем необходимые модули
import numpy as np
import random
import math

# генерация 100 случайных точек
X = [random.uniform(-10, 10) for _ in range(100)]
Y = [random.uniform(-10, 10) for _ in range(100)]
Z = [(math.sin(X[i]) * math.sin(Y[i])) for i in range(100)]

# пройдёмся циклом по коэффициентам процентов
for proc in range(0, 160, 10):
    # процент шума = proc
    # добавим шум в данные
    Z1 = [Zi + random.uniform(-(((max(Y) - min(Y)) * proc / 100) / 2),
                              (((max(Y) - min(Y)) * proc / 100) / 2)) for Zi in Z]
    data = np.array([X, Y, Z1]).T
    # добавим данные в файл, в название укажем процент шума
    with open(f'dataXYZ_{round(proc)}.txt', 'w') as f:
        [print(i, j, z, file=f) for i, j, z in data]
