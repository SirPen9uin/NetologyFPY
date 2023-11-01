class FlatIterator:

    def __init__(self, list_of_list):
        self.main_list = list_of_list

    def __iter__(self):
        self.iters_stack = [iter(self.main_list)]
        return self

    def __next__(self):
        while self.iters_stack:
            try:
                next_item = next(self.iters_stack[-1])
            except StopIteration:
                self.iters_stack.pop()
                continue

            if isinstance(next_item, list):
                self.iters_stack.append(iter(next_item))

            else:
                return next_item
        raise StopIteration


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()
