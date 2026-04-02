import numpy as np
import matplotlib.pyplot as plt

#np.random.seed(123)
samples = np.random.rand(1000)

plt.hist(samples, bins=20)
plt.title("Histogram z ustawionym ziarnem")
plt.xlabel("Wartość")
plt.ylabel("Liczba wystąpień")
plt.show()