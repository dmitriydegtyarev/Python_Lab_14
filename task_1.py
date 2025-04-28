import numpy as np
import matplotlib.pyplot as plt

# Збільшення плавності графіка
x = np.linspace(-2, 5, 500)
y = x * np.sin(5 * x)

plt.figure(figsize=(10, 6))

plt.plot(x, y, linestyle='-', color='blue', linewidth=2, label='y = x*sin(5*x)')

plt.xlabel("x", fontsize=14, color='red')
plt.ylabel("y", fontsize=14, color='red')

plt.title("Графік функції y = x*sin(5*x)", fontsize=16)

plt.legend()
plt.grid()
plt.show()