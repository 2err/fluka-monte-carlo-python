import numpy as np
import matplotlib.pyplot as plt

n=5000
num_experiments=20
a=0
b=1
exp_value=1/4
estim_values_trad=[]
stim_values_importance=[]

#Monte Carlo zwykłe

for i in range(num_experiments):
    x=np.random.uniform(a, b, n)
    esim_value=(b-a)*(np.mean(x**3))
    estim_values_trad.append(float(esim_value))

int_value=np.mean(estim_values_trad)
error_value=abs(exp_value-int_value)
std_value=np.std(estim_values_trad)
print(f"Średnia wartość to {int_value}, z błędem estymacji równym {error_value} i niepewnością {std_value}")

#Monte Carlo z importance sampling

for i in range(num_experiments):
    u=np.random.uniform(a, b, n)
    x=np.sqrt(u)
    p_x=2*x
    value_of_importance=np.mean((x**3)/p_x)
    esim_value_i=(b-a)* value_of_importance
    stim_values_importance.append(float(esim_value_i))

int_value_imp=np.mean(stim_values_importance)
error_value_imp=abs(exp_value-int_value_imp)
std_value_imp=np.std(stim_values_importance)
print(f"Średnia wartość to {int_value_imp}, z błędem estymacji równym {error_value_imp} i niepewnością {std_value_imp}")

if error_value_imp<error_value:
    print("Importance sampling  zwiększył poprawności estymacji całki")
else:
    print("Importance sampling nie zwiększył poprawności estymacji całki")

if std_value_imp<std_value:
    print("Importance sampling znacznie zmniejszył odchylenie standardowe")
else:
    print("Importance sampling nie zmiejszył odchylenia")