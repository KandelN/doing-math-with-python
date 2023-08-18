import matplotlib.pyplot as plt

from projectile import plot_path

velocities = [20, 30, 40 ]

plt.figure(dpi = 140, figsize = (13, 7))
for u in velocities:
    plot_path(u, 45)
plt.legend(['u20', 'u30', 'u40'], fontsize = 14)
plt.savefig("projectile_comp.png", bbox_inches = "tight")
