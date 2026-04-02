import numpy as np
import matplotlib.pyplot as plt

sampling_size=[100, 1000, 10000, 100000]
a=0
b=1
c=0
d=1
exact_value=0.25
integration_values=[]
error_values=[]


for n in sampling_size:
    x=np.random.uniform(a, b, n)
    y=np.random.uniform(c, d, n)
    f=x*y
    integral_value=(b-a)*(d-c)*(np.mean(f))
    integration_values.append(integral_value)
    print(f"***************************************************")
    print(f"Dla {n} wylosowanych próbek, wynik całkowania wynosi {integral_value}")
    error=abs(integral_value-exact_value)
    error_values.append(error)
    print(f"Błąd estymacji całki wynosi {error}")

small_error=min(error_values)
indeks=error_values.index(small_error)
best_integral=integration_values[indeks]
best_sampling=sampling_size[indeks]
print(f"***************************************************")
print(f"Najlepsze dopasowanie z błędem {small_error} wynosi {best_integral} dla próbek {best_sampling}.")

plt.scatter(sampling_size, integration_values, color="red")
plt.axhline(exact_value, color="blue")
plt.xlabel("Ilość próbek")
plt.ylabel("Estymacja całki")
plt.xscale("log")
plt.show()



