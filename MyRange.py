class MyRange():
    def __init__(self, args):
        if len(args) == 1:
            self.start = 0
            self.stop = args[0]
            self.step = 1
        elif len(args) == 2:
            self.start = args[0]
            self.stop = args[1]
            self.step = 1
        elif len(args) == 3:
            self.start = args[0]
            self.stop = args[1]
            self.step = args[2]
        else:
            raise ValueError("Invalid number of arguments")

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.stop:
            raise StopIteration

        current = self.start
        self.start += self.step
        return current

