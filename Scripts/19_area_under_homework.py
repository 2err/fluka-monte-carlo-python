import numpy as np
import matplotlib.pyplot as plt


sampling_size=[100, 1000, 10000, 100000]
exact_value = 2/3
fields=[]
errors=[]

for n in sampling_size:
    x=np.random.uniform(0, 1, n)
    y=np.random.uniform(0, 1, n)

    under_curve= y<= np.sqrt(x)
    point_inside=np.sum(under_curve)
    field=1*(point_inside/n)
    fields.append(field)
    error=abs(exact_value-field)
    errors.append(error)

    print("********************************************")
    print(f"Wyniki dla {n} prób")
    print(f"Ilość punktów w obszarze to: {point_inside}")
    print(f"Wartość pola to: {field}")
    print(f"Wartość błędu estymacji to {error}")

plt.scatter(sampling_size, fields, color="red")
plt.axhline(exact_value)
plt.xlabel("sampling size")
plt.ylabel("estimation of field")
plt.xscale("log")
plt.show()

best_error=np.min(errors)
ind=errors.index(best_error)
best_estimation=fields[ind]
best_size=sampling_size[ind]

print(f"Dla tego losowania, najlepszy wynik uzyskano dla {best_size}, gdzie wynik estymacji poda pod krzywą wynosi {best_estimation} z błędem estymacji równym {best_error}")