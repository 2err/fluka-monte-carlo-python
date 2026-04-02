import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
sample_sizes = [100, 1000, 10000, 100000]

n = 10000-

for i in sample_sizes:
    # losowanie punktów w kwadracie [0,1] x [0,1]
    x = np.random.uniform(0, 1, n)
    y = np.random.uniform(0, 1, n)

    # warunek: punkt znajduje się pod wykresem y = x^2
    inside_area = y <= x**2

    points_inside = np.sum(inside_area)

    # pole prostokąta = 1
    area_estimate = points_inside / n
    exact_value = 1 / 3
    error = abs(exact_value - area_estimate)

    print("Liczba punktów:", n)
    print("Punkty w obszarze:", points_inside)
    print("Estymacja pola:", area_estimate)
    print("Wartość dokładna:", exact_value)
    print("Błąd:", error)

    plt.figure(figsize=(6, 6))
    plt.scatter(x[inside_area], y[inside_area], s=2, label="W obszarze")
    plt.scatter(x[~inside_area], y[~inside_area], s=2, label="Poza obszarem")

    x_plot = np.linspace(0, 1, 200)
    y_plot = x_plot**2
    plt.plot(x_plot, y_plot, label="y = x^2")

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Estymacja pola pod wykresem y=x^2")
    plt.legend()
    plt.show()