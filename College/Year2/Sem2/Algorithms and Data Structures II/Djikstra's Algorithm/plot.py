import matplotlib
if __name__=="__main__":
    matplotlib.use("QtAgg")
import matplotlib.pyplot as plt

def plot_times(xlabel, ylabel, title, xvalues, *yvalues):
    for i in range(len(yvalues)):
        plt.plot(xvalues, yvalues[i])
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()
