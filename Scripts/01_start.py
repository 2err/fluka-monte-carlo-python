import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

losowania = np.random.rand(1000)

print("Średnia:", np.mean(losowania))
print("Minimum:", np.min(losowania))
print("Maksimum:", np.max(losowania))

plt.hist(losowania, bins=20)
plt.title("Histogram liczb losowych")
plt.xlabel("Wartość")
plt.ylabel("Liczba wystąpień")
plt.show()