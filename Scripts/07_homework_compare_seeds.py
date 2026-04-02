import numpy as np
import matplotlib.pyplot as plt

seed_sizes = [42, 123] #lista różnych liczebności próby
means=[]

for n in seed_sizes: #Bierzemy po kolei seedy
    np.random.seed(n)
    samples = np.random.rand(1000)

    plt.hist(samples, bins=20)
    plt.title(f"Histogram dla seed = {n}")
    plt.xlabel("Wartość")
    plt.ylabel("Liczba wystąpień")
    plt.show()
    means.append(np.mean(samples))


np.random.seed() #Brak seed
samples = np.random.rand(1000)

plt.hist(samples, bins=20)
plt.title(f"Histogram dla domyslnego seed")
plt.xlabel("Wartość")
plt.ylabel("Liczba wystąpień")
plt.show()
means.append(np.mean(samples))

means_float=[float(x) for x in means] #zmiana z float64 z numpy do float

print(means_float)