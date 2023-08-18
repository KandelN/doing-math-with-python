from visual import visualize
from stats_util import find_corr


if __name__ =="__main__":
    x = [2, 3, 5, 27, 18, 18]
    y = [2, 3, 11, 24, 78, 79]
    # y = [4, 6, 10, 54, 36, 36]
    print(find_corr(x, y))

    visualize(x = x, filename = "corr.png", s= 100)
