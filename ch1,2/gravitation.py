import matplotlib.pyplot as plt
from numpy import linspace

# Generate values
distances = list(range(100, 1001, 100))
distances_real = linspace(100, 1000, 10000)
G = 6.674*(10**-11)
m1 = 0.5
m2 = 1
Forces = [(G*m1*m2/dist**2) for dist in distances]
Forces_real = [(G*m1*m2/dist**2) for dist in distances_real]

# Visualize data
# Set screen size and title and axes labels for the plot.
plt.style.use("dark_background")
plt.figure(dpi=140, figsize= (13, 7))
plt.title("Gravitaional force and distance", fontsize = 24)
plt.xlabel("Distance (m)", fontsize = 14)
plt.ylabel("Gravitational Force(N)", fontsize = 14)

# Plot the points
plt.scatter(distances_real, Forces_real, s=0.1)
plt.plot(distances, Forces, "x", c= "white")

# Set size of tick labels.
plt.tick_params(axis = "both", which = "majaor", labelsize = 14)

plt.savefig("gravitation.png", bbox_inches = "tight")
