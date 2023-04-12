import pandas as pd
import numpy as np
import scipy.stats as sps


chat_id = 254567352 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    p_value = sps.permutation_test((x, y), lambda x, y, axis: np.mean(x, axis=axis) - np.mean(y, axis=axis), vectorized=True, n_resamples=5000, alternative='greater').pvalue
    alpha = 0.05
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    return p_value < alpha # Ваш ответ, True или False
