import matplotlib
import math
if __name__=="__main__":
    matplotlib.use("QtAgg")
import matplotlib.pyplot as plt

def plot_times(gridsizes, title, *args):
    for i in range(len(args)):
        plt.plot(gridsizes, args[i], label=f"{gridsizes[i]}")
    plt.xlabel("Grid Size")
    plt.ylabel("Execution Time")
    plt.title(title)
    plt.show()
