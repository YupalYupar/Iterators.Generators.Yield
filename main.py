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


# комперхеншн
kok = [item for item in FlatIterator(nested_list)]
print(f'Комперхеншн ==> {kok}')


def gen_list(a: list):  # Генератор 1
    yield [i for pok in a for i in pok]


def flat_generator(some_list: list):  # генератор 2
    for i in some_list:
        yield i


def flat_generator2(*args, **kwargs):  # генератор 3
    for hen in args, kwargs:
        for egg in hen:
            yield egg


if __name__ == "__main__":
    gun = [ball for ball in FlatIterator(nested_list)]
    print(f'итератор 1 ==> {gun}')

    for item in gen_list(nested_list):
        print(f'генератор 1 ==> {item}')

    for item in flat_generator(nested_list):
        print(f'генератор 2 ==> {item}')

    for item in flat_generator2(nested_list):
        print(f'генератор 3 ==> {item}')
