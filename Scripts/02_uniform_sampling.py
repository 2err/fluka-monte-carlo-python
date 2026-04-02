import numpy as np
import matplotlib.pyplot as plt

# 1. Losujemy 10 000 liczb z rozkładu jednostajnego [0, 1)
samples = np.random.rand(10000000)

# 2. Podstawowe statystyki
mean_value = np.mean(samples)
min_value = np.min(samples)
max_value = np.max(samples)
std_value = np.std(samples)

print("Średnia:", mean_value)
print("Minimum:", min_value)
print("Maksimum:", max_value)
print("Odchylenie standardowe:", std_value)

# 3. Histogram
plt.hist(samples, bins=30)
plt.title("Rozkład jednostajny U(0,1)")
plt.xlabel("Wartość")
plt.ylabel("Liczba wystąpień")
plt.show()