import matplotlib.pyplot as plt

def visualize(x = None, y = None, s = 1, title = "Scatter plot between x and y", xlabel = "x", ylabel = "y", filename = "defult_visual.png"):
    """
    Visualize data
    """
    # Set screen size and title and axes labels for the plot.
    plt.style.use("dark_background")
    plt.figure(dpi=140, figsize= (13, 7))
    plt.title(title +"\n", fontsize = 24)
    plt.xlabel("\n" + xlabel, fontsize = 14)
    plt.ylabel(ylabel + "\n", fontsize = 14)

    # Plot the points
    if x == None and y == None:
        raise ValueError("Supply at least one set of data.")
    elif y == None:
        y = list(range(1, len(x)+1, 1))
    elif x == None:
        x = list(range(1, len(y)+1, 1))

    plt.scatter(x, y, s=s)
    
    # Set size of tick labels.
    plt.tick_params(axis = "both", which = "majaor", labelsize = 14)

    plt.savefig(filename)
