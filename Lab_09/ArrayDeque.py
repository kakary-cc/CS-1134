import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()

class ArrayDeque:
    INITIAL_CAPACITY = 8

    def __init__(self):
        self.data_arr = make_array(ArrayDeque.INITIAL_CAPACITY)
        self.num_of_elems = 0
        self.front_ind = None

    def __len__(self):
        return self.num_of_elems

    def is_empty(self):
        return (len(self) == 0)

    def enqueue_first(self, elem):
        if (self.num_of_elems == len(self.data_arr)):
            self.resize(2 * len(self.data_arr))
        if (self.is_empty()):
            self.data_arr[0] = elem
            self.front_ind = 0
            self.num_of_elems += 1
        else:
            back_ind = (self.front_ind + self.num_of_elems) % len(self.data_arr)
            self.data_arr[back_ind] = elem
            self.num_of_elems += 1

    def enqueue_last(self, elem):
        if (self.num_of_elems == len(self.data_arr)):
            self.resize(2 * len(self.data_arr))
        if (self.is_empty()):
            self.data_arr[0] = elem
            self.front_ind = 0
            self.num_of_elems += 1
        else:
            back_ind = (self.front_ind + self.data_arr) % len(self.data_arr)
            self.data_arr[back_ind] = elem
            
            self.num_of_elems += 1

    def dequeue_first(self):
        if (self.is_empty()):
            raise Exception("Queue is empty")
        value = self.data_arr[self.front_ind]
        self.data_arr[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % len(self.data_arr)
        self.num_of_elems -= 1
        if(self.is_empty()):
            self.front_ind = None
        if((self.num_of_elems < len(self.data_arr) // 4) and
                (len(self.data_arr) > ArrayQueue.INITIAL_CAPACITY)):
            self.resize(len(self.data_arr) // 2)
        return value

    def dequeue_last(self):
        if (self.is_empty()):
            raise Exception("Queue is empty")
        value = self.data_arr[self.front_ind]
        self.data_arr[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % len(self.data_arr)
        self.num_of_elems -= 1
        if(self.is_empty()):
            self.front_ind = None
        if((self.num_of_elems < len(self.data_arr) // 4) and
                (len(self.data_arr) > ArrayQueue.INITIAL_CAPACITY)):
            self.resize(len(self.data_arr) // 2)
        return value

    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data_arr[self.front_ind]

    def last(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        back_ind = (self.front_ind + self.num_of_elems) % len(self.data_arr)
        return self.data_arr[back_ind]

    def resize(self, new_cap):
        old_data = self.data_arr
        new_data = make_array(new_cap)
        old_ind = self.front_ind
        for new_ind in range(self.num_of_elems):
            new_data[new_ind] = old_data[old_ind]
            old_ind = (old_ind + 1) % len(old_data)
        self.data_arr = new_data
        self.front_ind = 0