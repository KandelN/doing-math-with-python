import matplotlib.pyplot as plt
import sys

def n_fib(n):
    """
    Returns first n fibonacci terms
    """
    a = 0
    b = 1
    fibbs = [b]
    for i in range(n-1):
        c = a + b
        a = b
        b = c
        fibbs.append(c)
    return fibbs

def plot_path(n):
    """
    Plot graph x vs y when u and theta is provided.
    """
    
    #Generate Points
    fibbs = n_fib(n)
    x = []
    y = []
    for i in range(1,n):
        x.append(i-1)
        y.append(fibbs[i]/fibbs[i-1])

    # Visualize
    # Set screen size, title, axes labels
    plt.figure(dpi = 140, figsize = (13, 7))
    plt.style.use("dark_background")
    plt.title("Ratio of consecutive Fibonacci numbers",
        fontsize = 24)
    plt.xlabel("Term (n)", fontsize = 14)
    plt.ylabel("Ratio", fontsize = 14)

    # Set size of tick labels.
    plt.tick_params(axis="both", labelsize = 14)

    #Plot the points
    plt.plot(x, y)
    plt.savefig("fibb.png", bbox_inches = "tight")

if __name__ == "__main__":
    plot_path(int(sys.argv[1]))