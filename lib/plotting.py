import matplotlib.pyplot as plt
import numpy as np


def plotting(curve: np.ndarray, controll_points: list) -> None:
    fig, ax = plt.subplots(1)

    x, y = np.split(curve, [-1], axis=1)
    plt.plot(x, y, linestyle="-", color="darkorchid")

    for i in range(len(controll_points) - 1):
        P1, P2 = controll_points[i], controll_points[i + 1]
        plt.plot([P1[0], P2[0]], [P1[1], P2[1]], linestyle="-", color="gray")
        plt.plot(P1[0], P1[1], "o", color="red",
                 label=f"$P_{i}$ = ({P1[0]} | {P1[1]})")

    P = controll_points[-1]
    plt.plot(P[0], P[1], "o", color="red", label=f"$P_{i+1}$ = ({P[0]} | {P[1]})")

    plt.grid(True)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    ax.set_aspect('equal')
    plt.show()
    fig.savefig("bezier curve.png")
