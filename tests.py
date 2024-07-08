from heap import Heap
import random


def test_heap():
    def is_heap_correct(heap):
        for i in range(len(heap._list)):
            parent_index = ((i - 1) // heap._branches)
            if parent_index < 0:
                continue
            if heap._list[i] < heap._list[parent_index]:
                return False
        return True

    for number in [2, 5, 7]:  # Run the test 3 times for 3 branch options
        probe = random.sample(range(300000), 1000)
        heap = Heap(list=probe, branches=number)

        # Test pushing elements onto the heap
        for number in probe:
            heap.push(number)
            assert is_heap_correct(heap) is True

        # Test removing elements from the heap
        while len(heap._list) > 1:
            heap.remove_top()
            assert is_heap_correct(heap) is True
