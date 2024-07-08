import matplotlib.pyplot as plt
import os


def plot_result(probes: list, times: list[list], operation: str) -> None:
    cases = [2, 5, 7]
    plt.xlabel("Random probe size")
    plt.ylabel("Time (s)")
    plt.title(f'Time of {operation} operation on heaps')
    plt.grid(True)

    for i in range(3):
        plt.plot(probes, times[i],
                 label=f'{cases[i]}-ary heap {operation} time',
                 marker='o')

    # save result in plots directory
    directory = "plots"
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.legend()
    plt.savefig(os.path.join(directory, f"{operation}_plot.png"))
    plt.close()
