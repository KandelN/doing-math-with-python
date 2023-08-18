import sys
import matplotlib.pyplot as plt
from numpy import linspace
from math import radians, cos, sin

def coord_gen(u, theta):
    """
    Return list of coordinates when intial velocity and
    firing angle of projectile is given.
    """
    theta = radians(theta)
    g = 9.81

    # Time of flight
    T = 2*u*sin(theta)/g

    # Generate Values
    timeline = linspace(0, T, 1000)
    coords = x_coords, y_coords =[], []
    for t in timeline:
        x = u*cos(theta)*t
        y = u*sin(theta)*t - 0.5 * g * t**2
        x_coords.append(x)
        y_coords.append(y)

    return coords

def plot_path(u, theta):
    """
    Plot graph x vs y when u and theta is provided.
    """
    # Set screen size, title, axes labels
    plt.style.use("dark_background")
    plt.title(f"Path traced by a projectile \n(u={u}m/s2, theta={theta})",
        fontsize = 24)
    plt.xlabel("x in meters", fontsize = 14)
    plt.ylabel("y in meters", fontsize = 14)
    plt.axis( "equal")
    plt.grid(False)

    # Set size of tick labels.
    plt.tick_params(axis="both", labelsize = 14)

    #Plot the points
    x, y = coord_gen(u, theta)
    plt.scatter(x, y, s = 1)


if __name__ == "__main__":
    if len(sys.argv) > 3:
        sys.exit("Usage: python projectile.py [u] [theta]")
    u = float(sys.argv[1])
    theta = float(sys.argv[2])
    
    # Visualize
    plt.figure(dpi = 140, figsize = (13, 7))
    plot_path(u, theta)
    plt.savefig("projectile.png", bbox_inches = "tight")
