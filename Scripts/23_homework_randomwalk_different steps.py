import numpy as np
import matplotlib.pyplot as plt

n_particles=1000
steps=[10, 100, 1000]


end_positions=[]
end_std=[]

for n_steps in steps:
    final_positions = []

    for _ in range(n_particles):
        position = 0

        for _ in range(n_steps):
            step = np.random.choice([-1, 1])
            position += step

        final_positions.append(position)
    plt.hist(final_positions, bins=20)
    plt.xlabel("Położenie końcowe")
    plt.ylabel("Ilość cząstek")
    plt.title(f"{n_steps}")
    plt.show()

    end_positions.append(np.mean(final_positions))
    end_std.append(np.std(final_positions))
    print(f"Dla {n_steps} kroków, średnie położenie to {np.mean(final_positions)}, a rozrzut {np.std(final_positions)}")

if end_std[0]<end_std[1]<end_std[2]:
    print("Wraz ze zwiększaniem kroków w tym przypadku zwiększa się rozrzut")
elif end_std[0]>end_std[1]>end_std[2]:
    print("Wraz ze zwiększaniem kroków w tym przypadku zmniejsza się rozrzut")
else:
    print("Nie ma trendu w zmniejszeniu rozrzutu wraz ze zwiększeniem ilości kroków")


if end_positions[0]<end_positions[1]<end_positions[2]:
    print("Reguła jest taka, że dla kolejnych kroków próbkom udaje się średnio przejść najdalej")
elif 1>np.mean(end_positions)>-1:
    print("Odłegości na które przeszły próbki są bliskie 0")


