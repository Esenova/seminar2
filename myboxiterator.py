class MyBoxIterator:
    def __init__(self, plov):
        self.plov=plov

    def __iter__(self):
        return self

    def __next__(self):
        if self.plov is None:
            raise StopIteration
        else:
            data=self.plov.data
            self.plov=self.oppo.next
        return data  
