import matplotlib.pyplot as plt
import numpy as np

# створюємо масив x, уникаючи нуля
x = np.linspace(-2, 2, 400)
x = x[x != 0]

# формула функції
y = np.sin(x) * (1 / x) * np.cos(x**2 + 1/x)

# побудова графіку
plt.plot(x, y, label='Y(x)=sin(x)*(1/x)*cos(x² + 1/x)',
         color="purple", linewidth=2)

# назва графіка
plt.title('Графік функції Y(x)', fontsize=15)

# позначення осей
plt.xlabel('x', fontsize=12, color='blue')
plt.ylabel('Y(x)', fontsize=12, color='blue')

# легенда
plt.legend()

# сітка
plt.grid(True)

plt.show()
