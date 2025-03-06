class Element:
    def __init__(self, k, v, i):
        self._key = k
        self._value = v
        self._index = i

    def get_value(self):
        return self._value

    def __eq__(self, other):
        return self._key == other._key

    def __lt__(self, other):
        return self._key < other._key

    def __gt__(self, other):
        return self._key > other._key

    def _wipe(self):
        self._key = None
        self._value = None
        self._index = None

class APQUL:
    def __init__(self):
        self.list = []

    def length(self):
        return len(self.list)

    def add(self, key, item):
        element = Element(key, item, len(self.list))
        self.list.append(element)
        return element

    def minimum(self):
        minimum = self.list[0]
        for element in self.list:
            if element < minimum:
                minimum = element
        return minimum

    def remove_min(self):
        min_index = self.minimum()._index
        self.list[min_index], self.list[len(self.list)-1] = self.list[len(self.list)-1], self.list[min_index]
        self.list[min_index]._index = min_index
        return self.list.pop()

    def update_key(self, element, new_key):
        self.list[element._index]._key = new_key

    def get_key(self, element):
        return element._key

    def remove(self, element):
        i = element._index
        self.list[i], self.list[len(self.list)-1] = self.list[len(self.list)-1], self.list[i]
        self.list[i]._index = i
        self.list.pop()

##################################################################################################

class APQBH:
    def __init__(self):
        self.heap = []
        self.size = 0

    def length(self):
        return self.size

    def add(self, key, item):
        element = Element(key, item, self.size)
        self.heap.append(element)
        self.size += 1
        self.bubble_up(element)
        return element

    def bubble_up(self, element):
        if element._index == 0:
            return
        parent_index = (element._index - 1) // 2
        parent = self.heap[parent_index]
        if element._key < parent._key:
            self.heap[element._index], self.heap[parent_index] = self.heap[parent_index], self.heap[element._index]
            self.heap[element._index]._index, self.heap[parent_index]._index = self.heap[parent_index]._index, self.heap[element._index]._index
            self.bubble_up(self.heap[parent_index])

    def bubble_down(self, element):
        left_child_index = (element._index * 2) + 1
        right_child_index = (element._index * 2) + 2
        target = element
        print(f"Before swap: {[(v._key, v._value.__str__(), v._index) for v in self.heap]}")
        # print(f"Before swap: {[v._index for v in self.heap]}")
        if left_child_index < self.size - 1 and self.heap[left_child_index]._key < target._key:
            target = self.heap[left_child_index]
        if right_child_index < self.size - 1 and self.heap[right_child_index]._key < target._key:
            target = self.heap[right_child_index]
        if target == element:
            return
        self.heap[element._index]._index, self.heap[target._index]._index = self.heap[target._index]._index, self.heap[element._index]._index
        self.heap[element._index], self.heap[target._index] = self.heap[target._index], self.heap[element._index]
        print(f"After swap: {[(v._key, v._value.__str__(), v._index) for v in self.heap]}")
        self.bubble_down(self.heap[element._index])

    def minimum(self):
        return self.heap[0]

    def remove_min(self):
        root = self.heap[0]
        # print(self.heap[0]._index, self.heap[-1]._index)
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap[0]._index, self.heap[-1]._index = self.heap[-1]._index, self.heap[0]._index
        self.heap.pop()
        self.size -= 1
        if self.size > 0:
            self.bubble_down(self.heap[0])
        return root

    def update_key(self, element, key):
        if element._key == key:
            return
        elif element._key > key:
            self.bubble_up(self.heap[element._index])
        else:
            self.bubble_down(self.heap[element._index])

    def get_key(self, element):
        # print([v._index for v in self.heap])
        return element._key

    def remove(self, element):
        self.heap[-1], self.heap[element._index] = self.heap[element._index], self.heap[-1]
        self.heap[-1]._index, self.heap[element._index]._index = self.heap[element._index]._index, self.heap[-1]._index
        parent_index = (element._index - 1) // 2
        if element._key < self.heap[parent_index]._key:
            self.bubble_up(self.heap[element._index])
        else:
            self.bubble_down(self.heap[element._index])

