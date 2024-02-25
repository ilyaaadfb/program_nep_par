import math


def rmse(targets, predictions):
    squared_errors = [(p - t) ** 2 for p, t in zip(predictions, targets)]
    mean_squared_error = sum(squared_errors) / len(predictions)
    rmse = math.sqrt(mean_squared_error)

    return round(rmse, 5)
