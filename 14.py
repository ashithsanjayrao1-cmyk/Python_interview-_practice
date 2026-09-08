class FibonacciIterator:
    def __init__(self, limit: int):
        self.limit = limit
        self.count = 0
        self.a = 0
        self.b = 1


    def __iter__(self):

        return self

    def __next__(self):

        if self.count >= self.limit:
            raise StopIteration

        current_val = self.a

        self.a, self.b = self.b, self.a + self.b
        self.count += 1

        return current_val

for num in FibonacciIterator(limit = 7):
    print(num)
