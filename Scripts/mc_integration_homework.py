import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
sampling_size=[100, 1000, 10000, 100000]
a=0
b=1
estim_error_box=[]
estim_int_box=[]

for n in sampling_size:
    x=np.random.uniform(a,b,n)
    y=x**3
    estim_int=(b-a)*np.mean(y)
    estim_int_box.append(estim_int)
    print(f"**************************************")
    print(f"Estymacja całki z {n} punktami to {estim_int}")

    error_estim=abs(0.25-estim_int)
    print(f"Wartość błędu estymacji to {error_estim}")
    estim_error_box.append(error_estim)

plt.scatter(sampling_size, estim_int_box, color='red')
plt.axhline(0.25)
plt.xscale("log")
plt.xlabel("Ilość próbek")
plt.ylabel("Estymacja całki")
plt.show()


min_error=min(estim_error_box)
numer=estim_error_box.index(min_error)
best_estim=estim_int_box[numer]
best_match=sampling_size[numer]
print(f"**************************************")
print(f"Najlepsza estymacja jest dla {best_match} próbek i wynosi {best_estim}")