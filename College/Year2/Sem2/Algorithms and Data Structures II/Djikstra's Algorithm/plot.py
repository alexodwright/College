import matplotlib
# solve an error with the graph not showing
matplotlib.use("QtAgg")
import matplotlib.pyplot as plt

# plot any number of sets of y values against their x values
def plot_times(xlabel, ylabel, title, xvalues, *yvalues):
    # for however many sets of y values
    for i in range(len(yvalues)):
        plt.plot(xvalues, yvalues[i], label=f"{xvalues[i]}")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()
