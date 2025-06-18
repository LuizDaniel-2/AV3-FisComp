import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_sphere(ax, center, radius):
    u = np.linspace(0, 2 * np.pi, 20)
    v = np.linspace(0, np.pi, 20)
    x = center[0] + radius * np.outer(np.cos(u), np.sin(v))
    y = center[1] + radius * np.outer(np.sin(u), np.sin(v))
    z = center[2] + radius * np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(x, y, z, color='darkgray', alpha=0.6, edgecolor='darkgray')

# Parâmetros
L = 5
R = 0.3

# Criar figura 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_box_aspect([1, 1, 1])  # Proporções iguais

# Gerar esferas na malha 3D
for i in range(-L, L+1):
    for j in range(-L, L+1):
        for k in range(-L, L+1):
            plot_sphere(ax, (i, j, k), R)

# Ajustes de visualização
ax.set_xlim(-L-1, L+1)
ax.set_ylim(-L-1, L+1)
ax.set_zlim(-L-1, L+1)
ax.axis('off')  # Desliga os eixos
ax.grid('False')
plt.title('Grade de esferas 3D (lattice)')
plt.show()