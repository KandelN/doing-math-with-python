import sys
from stats_util import Stats

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit("Usage: python stats.py [number1] [number2] ...")
    nums = list(map(int, sys.argv[1:]))

    # Create a Stats object
    data = Stats(nums)

    # Display averages and dispersion.
    print("Frequency table:")
    data.print_frequency_table()
    print("\nMean\t:", data.get_mean())
    print("Median\t:", data.get_median())
    print("Mode\t:", end =" ")
    for n in data.get_modes():
        print(n, end=" ")
    print("\nRange\t:", data.get_range())
    print("Variance\t:", data.get_variance())
    print("Standard Dev\t:", data.get_sd())

    print("\n")
    data.get_grouped(200)
    data.plot_me(filename = "des_plot.png")
