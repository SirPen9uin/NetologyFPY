class FlatIterator:

    def __init__(self, list_of_list):
        self.main_list = list_of_list

    def __iter__(self):
        self.main_counter = 0
        self.sub_counter = 0
        return self

    def __next__(self):
        if self.main_counter == len(self.main_list):
            raise StopIteration
        list = self.main_list[self.main_counter]
        item = list[self.sub_counter]
        self.sub_counter += 1
        if self.sub_counter == len(list):
            self.main_counter += 1
            self.sub_counter = 0
        return item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
