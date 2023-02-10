class Array(object):
    def __init__(self, initialSize):
        self.__a = [None] * initialSize

        self.nItems = 0

    def __len__(self):

        return self.__nItems

    def get(self, n):

        if 0 <= n and n < self.__nItems:

            return self.__a[n]

    def set(self, n, value):
        if 0 <= n and n < self.__nItems:

            self.__a[n] = value

    def insert(self, item):
        self.__a[self.__nitems] = item
        self.__nItems += 1

    def find(self, item):
        for j in range(self.__nItems):
            if self.__a[j] == item:
                return j
        return -1

    def search(self, item):
        return self.get(self.find(item))

    def delete(self, item):
        for j in range(self.__nItems):
            if self.__a[j] == item:
                self.__nItems -= 1
                for k in range(j, self.__nItems):
                    self.__a[k] = self.__a[k+1]
                return True

        return False

    def traverse(self, function=print):
        for j in range(self.__nItems):
            function(self.__a[j])

    def removeDuplicates(self,nItems):
        return nItems

        print(nItems)
