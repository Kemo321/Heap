import math


class Heap:
    def __init__(self, list: list, branches: int) -> None:
        self._list = []
        self._branches = branches
        for number in list:
            self.push(number)

# Appends element and restores the heap
    def push(self, value: int) -> None:
        self._list.append(value)
        index = len(self._list) - 1
        parent_index = (index-1) // self._branches
        while parent_index >= 0:
            if value < self._list[parent_index]:
                self._list[index], self._list[parent_index] = self._list[parent_index], self._list[index]
                index = parent_index
                parent_index = ((index-1)//self._branches)
            else:
                break

# Removes min element and restores the heap
    def remove_top(self):
        if len(self._list) == 1:
            return self._list.pop()
        if len(self._list) < 1:
            return None
        min_element = self._list[0]
        self._list[0] = self._list.pop()
        child = [0] * (self._branches + 1)
        index = 0
        k = self._branches
        length = len(self._list)
        while True:
            for i in range(1, k + 1):
                child[i] = k * index + i if k * index + i < length else -1
            min_child, min_child_index = float("inf"), 0
            for i in range(1, k + 1):
                if child[i] != -1 and self._list[child[i]] < min_child:
                    min_child_index = child[i]
                    min_child = self._list[child[i]]
            if min_child == 9999999999999999999999999:
                break
            if self._list[index] > self._list[min_child_index]:
                self._list[index], self._list[min_child_index] = self._list[min_child_index], self._list[index]
            index = min_child_index
        return min_element


# Simple method to display the heap; readable only for heap size <= 31 and values < 100
    def display(self):

        level = 0
        index = 0

        while index < len(self._list):
            level_count = self._branches**level
            current_level_elements = self._list[index:index + level_count]
            line = ""
            parent_control_number = 0
            for x in current_level_elements:
                if parent_control_number % self._branches == 0 and level_count != 1:
                    line += "|"
                parent_control_number += 1
                line += f" {x} "
            if level_count != 1:
                line += "|"
            print(line.center(180))
            print("-"*200)
            index += level_count
            level += 1

# Simple method that works best with 2-ary heap
    def display_2_ary(self):

        def calculate_depth(n):
            return math.floor(math.log2(n)) + 1

        def print_spaces(count):
            return '  ' * count

        depth = calculate_depth(len(self._list))

        for level in range(depth):
            space_between = (2 ** (depth - level + 1)) - 1
            print(print_spaces(space_between // 2), end='')

            start_index = 2**level - 1
            end_index = min(len(self._list), 2**(level + 1) - 1)

            for i in range(start_index, end_index):
                print(self._list[i], end='')
                print(print_spaces(space_between), end='')

            print("\n")
