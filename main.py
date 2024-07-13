import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
dias = np.arange(1, 31)
casos_dengue = np.random.poisson(lam = 20, size = 30)

plt.figure(figsize=(10,5))
plt.plot(dias, casos_dengue, marker='o', linestyle='-', color = 'b', label='Casos de Dengue')
plt.xlabel('Dia do Mês')
plt.ylabel('Número de Casos')
plt.title("Casos de Dengue durante um mês ")
plt.legend()
plt.grid(True)
plt.show()