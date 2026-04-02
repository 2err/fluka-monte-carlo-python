import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

sample_sizes = [100, 10000]

for n in sample_sizes:
    samples = np.random.rand(n)

    mean_value = np.mean(samples)
    std_value = np.std(samples)
    error = abs(0.5 - mean_value)

    print(f"\nLiczba próbek: {n}")
    print("Średnia:", mean_value)
    print("Odchylenie standardowe:", std_value)
    print("Błąd względem 0.5:", error)

    plt.hist(samples, bins=20)
    plt.title(f"Histogram dla n = {n}")
    plt.xlabel("Wartość")
    plt.ylabel("Liczba wystąpień")
    plt.show()