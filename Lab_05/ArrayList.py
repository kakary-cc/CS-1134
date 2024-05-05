import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)() 
class ArrayList:
    def __init__(self, iter_collection = None):
        self.data_arr = make_array(1)
        self.capacity = 1
        self.n = 0
        if type(iter_collection) != type(None):
            self.extend(iter_collection)

    def __len__(self):
        return self.n

    def append(self, val):
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)
        self.data_arr[self.n] = val
        self.n += 1

    def resize(self, new_size):
        new_array = make_array(new_size)
        for i in range(self.n):
            new_array[i] = self.data_arr[i]
        self.data_arr = new_array
        self.capacity = new_size

    def __getitem__(self, ind):
        if ind < 0:
            ind = self.n - ind
        if ind >= self.n | ind < 0:
            raise IndexError('invalid index')
        return self.data_arr[ind]

    def remove(self, val):
        ind = 0
        for i in range(self.n):
            if self.data_arr[i] == val:
                ind = i
                break
        for i in range(ind, self.n - 1):
            self.data_arr[i] = self.data_arr[i + 1]
        self.n -= 1

    def removeAll(self, val):
        count = 0
        for i in range(self.n):
            if self.data_arr[i] == val:
                self.data_arr[i] = self.data_arr[i + count]
                count += 1
        self.n -= count

    def __setitem__(self, ind, val):
        if ind < 0:
            ind = self.n - ind
        if ind >= self.n | ind < 0:
            raise IndexError('invalid index')
        self.data_arr[ind] = val

    def __repr__(self):
        output = "["
        for i in range(self.n):
            if i:
                output += ", "
            output += str(self.data_arr[i])
        output += "]"
        return output

    def __add__(self, other):
        output = ArrayList()
        for i in range(self.n):
            output.append(self.data_arr[i])
        for i in range(other.n):
            output.append(other.data_arr[i])
        return output

    def __iadd__(self, other):
        for i in range(other.n):
            self.append(other.data_arr[i])
        return self

    def __mul__(self, k):
        output = ArrayList()
        for i in range(k):
            output.__iadd__(self)
        return output

    def __rmul__(self, k):
        return self.__mul__(self, k)

    def __iter__(self):
        for i in range(len(self)):
            yield self.data_arr[i]  #could also yield self[i]

    def extend(self, iter_collection):
        for elem in iter_collection:
            self.append(elem)

def main():
    a = ArrayList([4,5,4,52,4,3,21,4,3,5,46,5,42,41,5])
    print(a)
    b = ArrayList([5])
    print(b)
    print(a + b)
    a += b
    print(a)
    a.append(100100100)
    print(a)
    a.remove(52)
    print(a)

if __name__ == '__main__':
    main()