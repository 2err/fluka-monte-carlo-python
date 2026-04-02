import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

samples = np.random.rand(1000) #probka 1000 liczb

mean_value = np.mean(samples) #jaka jest przecietna

#zakres
min_value = np.min(samples)
max_value = np.max(samples)

#rozrzut
variance_value = np.var(samples)
std_value = np.std(samples)

print("Średnia:", mean_value)
print("Minimum:", min_value)
print("Maksimum:", max_value)
print("Wariancja:", variance_value)
print("Odchylenie standardowe:", std_value)
print("Błąd średniej względem 0.5:", abs(0.5 - mean_value))#jak srednia daleko od wartosci oczekiwanej

plt.hist(samples, bins=20)
plt.title("Histogram liczb losowych")
plt.xlabel("Wartość")
plt.ylabel("Liczba wystąpień")
plt.show()