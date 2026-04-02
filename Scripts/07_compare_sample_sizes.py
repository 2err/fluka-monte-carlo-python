import numpy as np
import matplotlib.pyplot as plt

sample_sizes = [100, 1000, 10000] #lista różnych liczebności próby

for n in sample_sizes: #Bierzemy po kolei liczebności
    np.random.seed(42) #Eksperyment ma być powtarzalny, więc ustawiamy seed
    samples = np.random.rand(n)

    plt.hist(samples, bins=20)
    plt.title(f"Histogram dla n = {n}")
    plt.xlabel("Wartość")
    plt.ylabel("Liczba wystąpień")
    plt.show()

    #Przy takim ustawieniu kodu, po wyłączeniu histogramuu włącza się kolejny