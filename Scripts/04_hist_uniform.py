import numpy as np
import matplotlib.pyplot as plt

samples = np.random.rand(100000)

plt.hist(samples, bins=20)
plt.title("Histogram rozkładu jednostajnego")
plt.xlabel("Wartość")
plt.ylabel("Liczba wystąpień")
plt.show()