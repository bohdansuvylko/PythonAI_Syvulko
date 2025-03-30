class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

class MyGenerator:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        for item in self.data:
            yield item

# Creating an iterator object
my_iterator = MyIterator([1, 2, 3, 4, 5])

# Iterating over the iterator object
for item in my_iterator:
    print(item)

# Creating a generator object
my_generator = MyGenerator([6, 7, 8, 9, 10])

# Iterating over the generator object
for item in my_generator:
    print(item)