import math
from nep_2D import nep_regression_2D
from get_points import get_data2D
from approx_2D import approx_2D
from nep_2D import nonparametric


def rmse(targets, predictions):
    squared_errors = [(p - t) ** 2 for p, t in zip(predictions, targets)]
    mean_squared_error = sum(squared_errors) / len(predictions)
    rmse = math.sqrt(mean_squared_error)

    return round(rmse, 5)


# def E(X, Y, c=None):
#     e = 0
#     for i in range(len(X)):
#         y_dop = nonparametric(X[i], c, X, Y)
#         e += (Y[i] - y_dop) ** 2
#     return round((e / len(X)) ** 0.5, 5)

# def E(x, y):
#     e = 0
#     for i in range(len(x)):
#         y_new = approx_2D(x, y)[1][i]
#         e += (y[i] - y_new) ** 2
#     return round((e / len(x)) ** 0.5, 5)


# print(get_data2D(f'dataXY_{120}.txt')[1])
# print(approx_2D(get_data2D(f'dataXY_{0}.txt')[0], get_data2D(f'dataXY_{0}.txt')[1])[1])

print("Апрокс0:",
      rmse(get_data2D(f'dataXY_{0}.txt')[1],
           nep_regression_2D(get_data2D(f'dataXY_{0}.txt')[0], get_data2D(f'dataXY_{0}.txt')[1])[1]))
print("Апрокс1:",
      rmse(get_data2D(f'dataXY_{10}.txt')[1],
           nep_regression_2D(get_data2D(f'dataXY_{10}.txt')[0], get_data2D(f'dataXY_{10}.txt')[1])[1]))
print("Апрокс2:",
      rmse(get_data2D(f'dataXY_{20}.txt')[1],
           nep_regression_2D(get_data2D(f'dataXY_{20}.txt')[0], get_data2D(f'dataXY_{20}.txt')[1])[1]))
print("Апрокс3:",
      rmse(get_data2D(f'dataXY_{30}.txt')[1],
           nep_regression_2D(get_data2D(f'dataXY_{30}.txt')[0], get_data2D(f'dataXY_{30}.txt')[1])[1]))
print("Апрокс4:",
      rmse(get_data2D(f'dataXY_{40}.txt')[1],
           nep_regression_2D(get_data2D(f'dataXY_{40}.txt')[0], get_data2D(f'dataXY_{40}.txt')[1])[1]))
print("Апрокс5:",
      rmse(get_data2D(f'dataXY_{50}.txt')[1],
           nep_regression_2D(get_data2D(f'dataXY_{50}.txt')[0], get_data2D(f'dataXY_{50}.txt')[1])[1]))
print("Апрокс6:",
      rmse(get_data2D(f'dataXY_{60}.txt')[1],
           nep_regression_2D(get_data2D(f'dataXY_{60}.txt')[0], get_data2D(f'dataXY_{60}.txt')[1])[1]))
print("Апрокс7:",
      rmse(get_data2D(f'dataXY_{70}.txt')[1],
           nep_regression_2D(get_data2D(f'dataXY_{70}.txt')[0], get_data2D(f'dataXY_{70}.txt')[1])[1]))
print("Апрокс8:",
      rmse(get_data2D(f'dataXY_{80}.txt')[1],
           nep_regression_2D(get_data2D(f'dataXY_{80}.txt')[0], get_data2D(f'dataXY_{80}.txt')[1])[1]))
print("Апрокс9:",
      rmse(get_data2D(f'dataXY_{90}.txt')[1],
           nep_regression_2D(get_data2D(f'dataXY_{90}.txt')[0], get_data2D(f'dataXY_{90}.txt')[1])[1]))
print("Апрокс10:",
      rmse(get_data2D(f'dataXY_{100}.txt')[1],
           nep_regression_2D(get_data2D(f'dataXY_{100}.txt')[0], get_data2D(f'dataXY_{100}.txt')[1])[1]))
print("Апрокс11:",
      rmse(get_data2D(f'dataXY_{110}.txt')[1],
           nep_regression_2D(get_data2D(f'dataXY_{110}.txt')[0], get_data2D(f'dataXY_{110}.txt')[1])[1]))
print("Апрокс12:",
      rmse(get_data2D(f'dataXY_{120}.txt')[1],
           nep_regression_2D(get_data2D(f'dataXY_{120}.txt')[0], get_data2D(f'dataXY_{120}.txt')[1])[1]))
print("Апрокс13:",
      rmse(get_data2D(f'dataXY_{130}.txt')[1],
           nep_regression_2D(get_data2D(f'dataXY_{130}.txt')[0], get_data2D(f'dataXY_{130}.txt')[1])[1]))
print("Апрокс14:",
      rmse(get_data2D(f'dataXY_{140}.txt')[1],
           nep_regression_2D(get_data2D(f'dataXY_{140}.txt')[0], get_data2D(f'dataXY_{140}.txt')[1])[1]))
print("Апрокс15:",
      rmse(get_data2D(f'dataXY_{150}.txt')[1],
           nep_regression_2D(get_data2D(f'dataXY_{150}.txt')[0], get_data2D(f'dataXY_{150}.txt')[1])[1]))


# print("Неп0:",
#       E(get_data2D(f'dataXY_{0}.txt')[1],
#            nep_regression_2D(get_data2D(f'dataXY_{0}.txt')[0], get_data2D(f'dataXY_{0}.txt')[1])[1],
#         nep_regression_2D(get_data2D(f'dataXY_{0}.txt')[0], get_data2D(f'dataXY_{0}.txt')[1])[2]))
# print("Неп1:",
#       E(get_data2D(f'dataXY_{10}.txt')[1],
#            nep_regression_2D(get_data2D(f'dataXY_{10}.txt')[0], get_data2D(f'dataXY_{10}.txt')[1])[1],
#         nep_regression_2D(get_data2D(f'dataXY_{10}.txt')[0], get_data2D(f'dataXY_{10}.txt')[1])[2]))
# print("Неп2:",
#       E(get_data2D(f'dataXY_{20}.txt')[1],
#            nep_regression_2D(get_data2D(f'dataXY_{20}.txt')[0], get_data2D(f'dataXY_{20}.txt')[1])[1],
#         nep_regression_2D(get_data2D(f'dataXY_{20}.txt')[0], get_data2D(f'dataXY_{20}.txt')[1])[2]))
# print("Неп3:",
#       E(get_data2D(f'dataXY_{30}.txt')[1],
#            nep_regression_2D(get_data2D(f'dataXY_{30}.txt')[0], get_data2D(f'dataXY_{30}.txt')[1])[1],
#         nep_regression_2D(get_data2D(f'dataXY_{30}.txt')[0], get_data2D(f'dataXY_{30}.txt')[1])[2]))
# print("Неп4:",
#       E(get_data2D(f'dataXY_{40}.txt')[1],
#            nep_regression_2D(get_data2D(f'dataXY_{40}.txt')[0], get_data2D(f'dataXY_{40}.txt')[1])[1],
#         nep_regression_2D(get_data2D(f'dataXY_{40}.txt')[0], get_data2D(f'dataXY_{40}.txt')[1])[2]))
# print("Неп5:",
#       E(get_data2D(f'dataXY_{50}.txt')[1],
#            nep_regression_2D(get_data2D(f'dataXY_{50}.txt')[0], get_data2D(f'dataXY_{50}.txt')[1])[1],
#         nep_regression_2D(get_data2D(f'dataXY_{50}.txt')[0], get_data2D(f'dataXY_{50}.txt')[1])[2]))
# print("Неп6:",
#       E(get_data2D(f'dataXY_{60}.txt')[1],
#            nep_regression_2D(get_data2D(f'dataXY_{60}.txt')[0], get_data2D(f'dataXY_{60}.txt')[1])[1],
#         nep_regression_2D(get_data2D(f'dataXY_{60}.txt')[0], get_data2D(f'dataXY_{60}.txt')[1])[2]))
# print("Неп7:",
#       E(get_data2D(f'dataXY_{70}.txt')[1],
#            nep_regression_2D(get_data2D(f'dataXY_{70}.txt')[0], get_data2D(f'dataXY_{70}.txt')[1])[1],
#         nep_regression_2D(get_data2D(f'dataXY_{70}.txt')[0], get_data2D(f'dataXY_{70}.txt')[1])[2]))
# print("Неп8:",
#       E(get_data2D(f'dataXY_{80}.txt')[1],
#            nep_regression_2D(get_data2D(f'dataXY_{80}.txt')[0], get_data2D(f'dataXY_{80}.txt')[1])[1],
#         nep_regression_2D(get_data2D(f'dataXY_{80}.txt')[0], get_data2D(f'dataXY_{80}.txt')[1])[2]))
# print("Неп9:",
#       E(get_data2D(f'dataXY_{90}.txt')[1],
#            nep_regression_2D(get_data2D(f'dataXY_{90}.txt')[0], get_data2D(f'dataXY_{90}.txt')[1])[1],
#         nep_regression_2D(get_data2D(f'dataXY_{90}.txt')[0], get_data2D(f'dataXY_{90}.txt')[1])[2]))
# print("Неп10:",
#       E(get_data2D(f'dataXY_{100}.txt')[1],
#            nep_regression_2D(get_data2D(f'dataXY_{100}.txt')[0], get_data2D(f'dataXY_{100}.txt')[1])[1],
#         nep_regression_2D(get_data2D(f'dataXY_{100}.txt')[0], get_data2D(f'dataXY_{100}.txt')[1])[2]))
# print("Неп11:",
#       E(get_data2D(f'dataXY_{110}.txt')[1],
#            nep_regression_2D(get_data2D(f'dataXY_{110}.txt')[0], get_data2D(f'dataXY_{110}.txt')[1])[1],
#         nep_regression_2D(get_data2D(f'dataXY_{110}.txt')[0], get_data2D(f'dataXY_{110}.txt')[1])[2]))
# print("Неп12:",
#       E(get_data2D(f'dataXY_{120}.txt')[1],
#            nep_regression_2D(get_data2D(f'dataXY_{120}.txt')[0], get_data2D(f'dataXY_{120}.txt')[1])[1],
#         nep_regression_2D(get_data2D(f'dataXY_{120}.txt')[0], get_data2D(f'dataXY_{120}.txt')[1])[2]))
# print("Неп13:",
#       E(get_data2D(f'dataXY_{130}.txt')[1],
#            nep_regression_2D(get_data2D(f'dataXY_{130}.txt')[0], get_data2D(f'dataXY_{130}.txt')[1])[1],
#         nep_regression_2D(get_data2D(f'dataXY_{130}.txt')[0], get_data2D(f'dataXY_{130}.txt')[1])[2]))
# print("Неп14:",
#       E(get_data2D(f'dataXY_{140}.txt')[1],
#            nep_regression_2D(get_data2D(f'dataXY_{140}.txt')[0], get_data2D(f'dataXY_{140}.txt')[1])[1],
#         nep_regression_2D(get_data2D(f'dataXY_{140}.txt')[0], get_data2D(f'dataXY_{140}.txt')[1])[2]))
# print("Неп15:",
#       E(get_data2D(f'dataXY_{150}.txt')[1],
#            nep_regression_2D(get_data2D(f'dataXY_{150}.txt')[0], get_data2D(f'dataXY_{150}.txt')[1])[1],
#         nep_regression_2D(get_data2D(f'dataXY_{150}.txt')[0], get_data2D(f'dataXY_{150}.txt')[1])[2]))

# Апрокс0: 0.68537
# Апрокс1: 0.69451
# Апрокс2: 0.6993
# Апрокс3: 0.71667
# Апрокс4: 0.72279
# Апрокс5: 0.71271
# Апрокс6: 0.79902
# Апрокс7: 0.8001
# Апрокс8: 0.80268
# Апрокс9: 0.85322
# Апрокс10: 0.91458
# Апрокс11: 0.95204
# Апрокс12: 0.9636
# Апрокс13: 1.09179
# Апрокс14: 1.0513
# Апрокс15: 1.07723


# Апрокс0: 0.0
# Апрокс1: 0.05529
# Апрокс2: 0.12521
# Апрокс3: 0.16891
# Апрокс4: 0.22393
# Апрокс5: 0.28138
# Апрокс6: 0.33927
# Апрокс7: 0.40005
# Апрокс8: 0.47238
# Апрокс9: 0.50524
# Апрокс10: 0.54626
# Апрокс11: 0.64742
# Апрокс12: 0.62432
# Апрокс13: 0.78806
# Апрокс14: 0.85832
# Апрокс15: 0.81675

