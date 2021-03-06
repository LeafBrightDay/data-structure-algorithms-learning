class MaxHeap:
    def __init__(self, array=None):
        if array:
            self.heap = self._max_heapify(array)
        else:
            self.heap = []

    def _sink(self, array, i):
        # move node down the tree
        left, right = 2 * i + 1, 2 * i + 2   ##index out of range when no right children
        max_index = i
        # should compare two chidren then determine which one to swap with
        flag = array[left] > array[right]
        if left < len(array) and array[left] > array[max_index] and flag:
            max_index = left
        if right < len(array) and array[right] > array[max_index] and not flag:
            max_index = right
        if max_index != i:
            array[i], array[max_index] = array[max_index], array[i]
            self._sink(array, max_index)

    def _swim(self, array, i):
        # move node up the tree
        if i == 0:
            return
        father = int((i - 1) / 2)
        if array[father] < array[i]:
            array[father], array[i] = array[i], array[father]
            self._swim(array, father)

    def _max_heapify(self, array):
        for i in range(int(len(array) / 2), -1, -1):
            self._sink(array, i)
        return array

    def push(self, item):
        self.heap.append(item)
        self._swim(self.heap, len(self.heap) - 1)

    def pop(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        item = self.heap.pop()
        self._sink(self.heap, 0)###after pop, no right children
        return item

    def items(self):
        return self.heap
