def identity(x):
    return x

class OrderedRecordArray(object):
    def __init__(self, initialSize, key=identity):
        self.__a = [None] * initialSize

        self.__nItems = 0

        self.__key = key

    def __len__(self):

        return self.__nItems

    def get(self, n):

        if n >= 0 and n < self.__nItems:

            return self.__a[n]

        raise IndexError("Index" + str(n) + " is out of range")

    def traverse(self, function=print):
        for j in range(self.__nItems):
            function(self.__a[j])

    def __str__(self):

        ans = "["

        for i in range(self.__nItems):
            if len(ans) > 1:

               ans += ", "
            ans += str(self.__a[i])

            ans += "]"

            return ans

    def find(self, key):

        lo = 0
        hi = self.__nItems-1

        while lo <= hi:
            mid = (lo + hi) // 2

            if self.__key(self.__a[mid]) == key:
                return mid

            elif self.__key(self.__a[mid]) < key:

                lo = mid + 1

            else:
                hi=mid - 1

        return lo

    def search(self, key):
        idx = self.find(key)

        if idx < self.__nItems and self.__key(self.__a[idx]) == key:
            return self.__a[idx]

    def insert(self, item):

        if self.__nItems >= len(self.__a):
            raise Exception("Array overflow")

        j = self.find(self.__key(item))

        for k in range(self.__nItems, j, -1):

            self.__a[k] = self.__a[k-1]

        self.__a[j] = item
        self.__nItems += 1

    def delete(self, item):
        j = self.find(self.__key(item))
        if j < self.__nItems and self.__a[j] == item:
            self.__nItems -= 1
            for k in range(j, self.__nItems):

                self.__a[k] = self.__a[k+1]
            return True
        return False
        
    def __init__(self, max_size):
        self.array = []
        self.max_size = max_size


    def insert(self, item):
        if len(self.array) == self.max_size:
            new_array = [None] * (2 * self.max_size)
            for i in range(self.max_size):
                new_array[i] = self.array[i]
            self.array = new_array
            self.max_size = 2 * self.max_size
        self.array[len(self.array)] = item