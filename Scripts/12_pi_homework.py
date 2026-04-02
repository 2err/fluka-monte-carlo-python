import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
sample_sizes=[100, 1000, 10000, 50000]
pi_box=[]
estim_box=[]

for n in sample_sizes:
    x=np.random.rand(n)
    y=np.random.rand(n)
    circle=x**2+y**2<=1
    points_circle=sum(circle)
    pi_estimates=(points_circle/n)*4
    mean_pi=np.mean(pi_estimates)
    print(f"Wartość obliczonej liczby pi to {mean_pi}")
    error=abs(np.pi-mean_pi)
    print(f"Błąd estymacji = {error}")
    pi_box.append(float(mean_pi))
    estim_box.append(float(error))

plt.plot(sample_sizes, pi_box, marker='o')
plt.xlabel("Ilość prób")
plt.ylabel("Estymacja pi")
plt.xscale("log")
plt.axhline(np.pi)
plt.show()

min_error=np.min(estim_box)
indeks=estim_box.index(min_error)
min_pi=pi_box[indeks]
proby=sample_sizes[indeks]

print(f"Najlepszy wynik estymacji to {min_error}, występujący przy Pi równej {min_pi}, przy ilości prób {proby}")

