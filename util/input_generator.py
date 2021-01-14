import numpy as np


def generate_random_list(count: int) -> list:
    """入力の要素数で1～10,000までの整数が入ったリストを生成する"""
    initial_list = list(np.random.randint(low=1, high=10000, size=count))
    print(f'Initial list: {initial_list}')
    return initial_list
