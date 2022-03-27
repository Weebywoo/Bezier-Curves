import numpy as np
from typing import Union

def create_bezier_curves(controll_points: list, step_size: float) -> Union[np.ndarray, None]:
    if len(controll_points) % 4 != 3 and len(controll_points) != 4:
        return None

    bezier_curves = [
        cubic_bezier_curve(controll_points[index: index + 4], step_size)
        for index in range(0, len(controll_points), 3)
    ]

    return np.concatenate(tuple(bezier_curves))

def cubic_bezier_curve(controll_points: list, step_size: float) -> np.ndarray:
    p = np.zeros((int(1 / step_size) + 1, 2))

    for i, t in enumerate(np.arange(0, 1 + step_size, step_size)):
        p[i] += bezier_step(controll_points, t)

    return p


def bezier_step(controll_points: list, t: float) -> np.ndarray:

    for _ in range(len(controll_points) - 1):
        controll_points = [lerp(controll_points[i], controll_points[i + 1], t)
                           for i in range(len(controll_points) - 1)]

    return controll_points[0]


def lerp(a: np.ndarray, b: np.ndarray, t: float) -> np.ndarray:
    return a + ((b - a) * t)


# def fit_bezier_curves(points_to_fit: list, step_size: float) -> Union[np.ndarray, None]:
#     if len(controll_points) % 4 != 3 and len(controll_points) != 4:
#         return None
    
#     bezier_curves = [
#         fit_cubic_bezier_curve(points_to_fit[index: index + 4], step_size)
#         for index in range(0, len(points_to_fit), 3)
#     ]
    
#     return np.concatenate(tuple(bezier_curves))

# def fit_cubic_bezier_curve(points_to_fit: list, step_size: float) -> np.ndarray:
#     return None