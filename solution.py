import pandas as pd
import numpy as np
from scipy.stats import permutation_test
from scipy.stats import mannwhitneyu

chat_id = 5351182285 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    res = mannwhitneyu(x, y, alternative="greater", method="exact")
    Result = bool (res.pvalue<=0.09)
    return Result # Ваш ответ, True или False
