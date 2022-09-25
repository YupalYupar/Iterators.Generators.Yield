nested_list = [['a', 'b', 'c'], ['d', 'e', 'f', 'h', False], [1, 2, None]]


class FlatIterator:
    def __init__(self, tuk: list):
        self.tuk = tuk
        self.cursor = -1
        self.tuk_cursor = 0
        self.tuk_len = len(self.tuk)

    def __iter__(self):
        self.cursor += 1
        self.tuk_cursor = 0
        return self

    def __next__(self):
        if self.tuk_cursor == len(self.tuk[self.cursor]):
            iter(self)
        if self.cursor == self.tuk_len:
            raise StopIteration
        self.tuk_cursor += 1
        return self.tuk[self.cursor][self.tuk_cursor - 1]


def gen_list(a: list):
    yield [i for pok in a for i in pok]


if __name__ == "__main__":
    gun = [ball for ball in FlatIterator(nested_list)]
    print(gun)

    for item in gen_list(nested_list):
        print(item)
