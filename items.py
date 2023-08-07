import numpy as np


class Kernel:
    Laplacian = np.array([
        [0, 1, 0],
        [1, -4, 1],
        [0, 1, 0]
    ])

    Sharpen = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ])

    Blur = (1/9) * np.array([
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ])
