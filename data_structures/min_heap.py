class MinHeap:
    def __init__(self):
        self.heap=[]

    def is_empty(self):
        return len(self.heap) == 0

    def push(self, priority, value):
        self.heap.append((priority, value))
        self.__bubble__up(len(self.heap)-1)

    def pop(self):
        if self.is_empty():
            raise IndexError(
                "pop from an empty heap"
            )
        smallest = self.heap[0]
        last_item = self.heap.pop()
        if self.heap:
            self.heap[0] = last_item
            self._sink_down(0)
            return smallest

    def _parent(self, i):
        return (i-1)//2

    def _left_child(self,i):
        return 2*i + 1

    def _right_child(self,i):
        return 2*i+2

    def _bubble_up(self,i):
        while i>0:
            parent_i = self._parent(i)
            if self.heap[i][0]<self.heap[parent_i][0]:
                self.heap[i],self.heap[parent_i] = self.heap[parent_i],self.heap[i]
                i=parent_i
            else:
                break

    def _sink_down(self,i):
        size = len(self.heap)
        while True:
            left_i = self._left_child(i)
            right_i = self._right_child(i)
            smallest = i

            if left_i < size and self.heap[left_i][0] < self.heap[smallest][0]:
                smallest = left_i
            if right_i < size and self.heap[right_i][0] < self.heap[smallest][0]:
                smallest = right_i

            if smallest == i:
                break    

            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest