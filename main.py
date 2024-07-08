from heap import Heap
from plot import plot_result
import random
import time
import gc


def main():
    gc.disable()
    test_case = random.sample(range(300000), 100000)
    probes = [i * 10000 for i in range(1, 11)]
    creation_times = []
    remove_top_times = []
    for branch in [2, 5, 7]:
        case = []
        case2 = []
        for k in range(10):
            start = time.time()
            Heap(list=test_case[:k*10000], branches=branch)
            case.append(float(round(time.time() - start, 4)))
        creation_times.append(case)
        heap = Heap(list=test_case, branches=branch)
        start = time.time()
        for k in range(100000):
            heap.remove_top()
            if k % 10000 == 0:
                case2.append(time.time() - start)
        remove_top_times.append(case2)
    plot_result(probes=probes, times=creation_times, operation="create")
    plot_result(probes=probes, times=remove_top_times, operation="remove top")


if __name__ == "__main__":
    main()
