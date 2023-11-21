import numpy as np


def reverse_array(arr: np.array):
    arr = arr.copy()
    arr_len = len(arr)
    for i in range(arr_len // 2):
        arr[i], arr[arr_len - 1 - i] = arr[arr_len - 1 - i], arr[i]
    return arr
