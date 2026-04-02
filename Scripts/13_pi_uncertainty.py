import numpy as np
import matplotlib.pyplot as plt

n = [1000, 10000]
num_experiments = 20

pi_results = []

for i in n:
    for _ in range(num_experiments):
        x = np.random.rand(i)
        y = np.random.rand(i)

        inside_circle = x**2 + y**2 <= 1
        points_inside = np.sum(inside_circle)

        pi_estimate = 4 * points_inside / i
        pi_results.append(pi_estimate)

    mean_pi = np.mean(pi_results)
    std_pi = np.std(pi_results)
    min_pi = np.min(pi_results)
    max_pi = np.max(pi_results)

    print("Liczba punktów w jednym eksperymencie:", i)
    print("Liczba powtórzeń eksperymentu:", num_experiments)
    print("Średnia estymacja pi:", mean_pi)
    print("Odchylenie standardowe:", std_pi)
    print("Minimum:", min_pi)
    print("Maksimum:", max_pi)
    print("Błąd średniej względem np.pi:", abs(np.pi - mean_pi))

    plt.hist(pi_results, bins=10)
    plt.title("Rozrzut wyników estymacji pi")
    plt.xlabel("Wartość estymacji pi")
    plt.ylabel("Liczba wystąpień")
    plt.show()