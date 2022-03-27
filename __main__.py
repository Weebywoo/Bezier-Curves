import numpy as np
from bezier_curves.lib.plotting import plotting
from bezier_curves.lib.bezier_curve import create_bezier_curves


def main() -> None:
    step_size = 0.01
    controll_points = np.random.randint(0, 25, (4, 2))  # [
    #     np.array([0, 1]),
    #     np.array([0, 2]),
    #     np.array([1, 2]),
    #     np.array([1, 1]),
    #     np.array([1, 0]),
    #     np.array([0, 0]),
    #     np.array([0, 1]),
    # ]

    bezier_curves = create_bezier_curves(controll_points, step_size)
    plotting(bezier_curves, controll_points)


if __name__ == "__main__":
    main()
